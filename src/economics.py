"""Lab 13 · Thành viên 1 (TV1): Mô hình chi phí và phân tích độ nhạy (CP1–CP2).
Chạy trong thư mục src/: python economics.py
"""
import os
import pandas as pd

GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH = 40_000_000  # đồng / tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1.0 / p
    return (1.0 - (1.0 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1.0 - (1.0 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_viec(p, k) / ti_le_thanh_cong(p, k) if False else so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần -> 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng -> 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần -> 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps."""
    r = runs
    q = reqs
    if max_lan_chay is not None:
        r = runs[runs['attempt'] <= max_lan_chay]
        q = reqs.copy()
        q.loc[q['so_lan_chay'] > max_lan_chay, 'ket_qua'] = 'chuyen_nhan_vien'

    token = (r['tokens_in'].sum() / 1000.0) * gia_vao + (r['tokens_out'].sum() / 1000.0) * gia_ra
    tool = r['tool_calls'].sum() * gia_tool
    xem_lai = q['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = q['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = token + tool + xem_lai + lam_lai
    thanh_cong = int((q['ket_qua'] == 'thanh_cong').sum())
    cps = tong / thanh_cong if thanh_cong > 0 else float('inf')

    return {
        'token': token,
        'tool': tool,
        'xem_lai': xem_lai,
        'lam_lai': lam_lai,
        'tong': tong,
        'thanh_cong': thanh_cong,
        'cps': cps,
    }


def _loc_theo_loai(runs, reqs, loai_list):
    q = reqs[reqs['loai'].isin(loai_list)]
    r = runs[runs['request_id'].isin(q['request_id'])]
    return r, q


def chay_phan_tich(data_dir='.'):
    runs = pd.read_csv(os.path.join(data_dir, 'logix_runs.csv'))
    reqs = pd.read_csv(os.path.join(data_dir, 'logix_requests.csv'), keep_default_na=False)

    print('=== A1: KIỂM THỬ ĐÁP ÁN BIẾT TRƯỚC ===')
    kiem_tra_dap_an_biet_truoc()
    print(f'so_lan_chay_ky_vong(0.8, 2) = {so_lan_chay_ky_vong(0.8, 2):.4f}')
    print(f'so_lan_chay_ky_vong(0.8)    = {so_lan_chay_ky_vong(0.8):.4f}')
    print(f'he_so_cps(0.8, 3)           = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.4f}')

    print('\n=== A2: MÔ HÌNH CHI PHÍ TỪ TRACE ===')
    kq = mo_hinh(runs, reqs)
    for k, v in kq.items():
        print(f'{k:12s}: {v:>14,.2f}')
    r_retry = runs[runs['attempt'] > 1]
    token_retry = (r_retry['tokens_in'].sum() / 1000.0) * GIA_VAO + (r_retry['tokens_out'].sum() / 1000.0) * GIA_RA
    tool_retry = r_retry['tool_calls'].sum() * GIA_TOOL
    hoa_don_moi_yc = (kq['token'] + kq['tool']) / len(reqs)
    print(f'retry_token+tool (attempt>1): {token_retry + tool_retry:,.2f}')
    print(f'hoa_don / so_yeu_cau        : {hoa_don_moi_yc:,.2f}')
    print(f'cps / hoa_don_moi_yc        : {kq["cps"] / hoa_don_moi_yc:.2f}x')

    print('\n=== A3: TÁCH THEO LOẠI YÊU CẦU ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r_l, q_l = _loc_theo_loai(runs, reqs, [loai])
        k_l = mo_hinh(r_l, q_l)
        ti_le_tc = k_l['thanh_cong'] / len(q_l) * 100
        tb_chay = q_l['so_lan_chay'].mean()
        print(f'{loai:10s} | n={len(q_l):4d} | tc={ti_le_tc:5.1f}% | runs/req={tb_chay:.2f} | cps={k_l["cps"]:>10,.0f} | vs 12k: {k_l["cps"]-BASELINE:+,.0f}')

    print('\n=== A4: CHI PHÍ CỐ ĐỊNH (noi_dia + hang_nang) ===')
    r_nh, q_nh = _loc_theo_loai(runs, reqs, ['noi_dia', 'hang_nang'])
    k_nh = mo_hinh(r_nh, q_nh)
    ti_le_nh = len(q_nh) / len(reqs)
    ti_le_tc_nh = k_nh['thanh_cong'] / len(q_nh)
    for vol in [45000, 22500]:
        yc_pham_vi = vol * ti_le_nh
        tc_thang = yc_pham_vi * ti_le_tc_nh
        co_dinh_moi_viec = CHI_PHI_CO_DINH / tc_thang
        tong_moi_viec = k_nh['cps'] + co_dinh_moi_viec
        print(f'vol={vol:5d} | yc_pv={yc_pham_vi:7,.0f} | tc={tc_thang:7,.0f} | fixed/tc={co_dinh_moi_viec:6,.0f} | total_cps={tong_moi_viec:7,.0f} | vs 12k: {tong_moi_viec-BASELINE:+,.0f}')

    print('\n=== B1: ĐỘ NHẠY TỪNG YẾU TỐ ===')
    base_cps = kq['cps']
    kich_ban = [
        ('Giá token x2', dict(gia_vao=52, gia_ra=260)),
        ('Giá token /2', dict(gia_vao=13, gia_ra=65)),
        ('Tỉ lệ xem lại x2', dict(he_so_xem_lai=2.0)),
        ('Tỉ lệ xem lại /2', dict(he_so_xem_lai=0.5)),
        ('Số ca làm lại x2', dict(he_so_lam_lai=2.0)),
        ('Số ca làm lại /2', dict(he_so_lam_lai=0.5)),
        ('Lương NV +25% (2500)', dict(luong_phut=2500)),
        ('Tối đa 2 lần chạy', dict(max_lan_chay=2)),
        ('Tối đa 1 lần chạy', dict(max_lan_chay=1)),
    ]
    for ten, kw in kich_ban:
        res = mo_hinh(runs, reqs, **kw)
        pct = (res['cps'] - base_cps) / base_cps * 100
        print(f'{ten:24s} | cps={res["cps"]:>9,.0f} | {pct:+6.1f}%')

    print('\n=== B2: ĐỔI MỘT CẶP ===')
    res_b2 = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2.0)
    print(f'Token x2 + Xem lại x2    | cps={res_b2["cps"]:>9,.0f} | {(res_b2["cps"]-base_cps)/base_cps*100:+6.1f}%')

    print('\n=== B3: GIỚI HẠN CHẠY LẠI ===')
    for lim in [1, 2, 3]:
        res = mo_hinh(runs, reqs, max_lan_chay=lim)
        khong_tc = len(reqs) - res['thanh_cong']
        chi_phi_he_thong = res['tong'] + khong_tc * BASELINE
        print(f'{lim} lần | tong_tl={res["tong"]:>11,.0f} | fail={khong_tc:3d} | he_thong={chi_phi_he_thong:>11,.0f} | cps={res["cps"]:>7,.0f}')

    print('\n=== B4: XEM LẠI 100% (noi_dia + hang_nang) ===')
    da_xem = q_nh[q_nh['phut_xem_lai_simulated'] > 0]['phut_xem_lai_simulated']
    tb_phut_xem = da_xem.mean()
    tong_xem_100 = len(q_nh) * tb_phut_xem * LUONG_PHUT
    tong_100 = k_nh['token'] + k_nh['tool'] + tong_xem_100 + k_nh['lam_lai']
    cps_100 = tong_100 / k_nh['thanh_cong']
    print(f'tb_phut_xem_lai={tb_phut_xem:.2f} | cps_100%={cps_100:,.0f} | vs 12k: {cps_100-BASELINE:+,.0f}')


if __name__ == '__main__':
    chay_phan_tich('.')
