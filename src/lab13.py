"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
from statistics import NormalDist
import pandas as pd
from statsmodels.stats.proportion import proportion_effectsize
from statsmodels.stats.power import NormalIndPower

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    return 1 / p if k is None else (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    return 1.0 if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong,
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    print('=== A1 ===')
    print(f'p=0.8, k=2:   {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'p=0.8, k=inf: {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'he_so(0.8,3): {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    kiem_tra_dap_an_biet_truoc()

    print('\n=== A2 ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    khong_tc = len(reqs) - ket_qua['thanh_cong']
    he_thong_yc = (ket_qua['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'cps / hoa_don:   {ket_qua["cps"] / ket_qua["hoa_don_moi_yc"]:.1f}x')
    print(f'ti_trong_xem:    {ket_qua["xem_lai"] / ket_qua["tong"] * 100:.1f}%')
    print(f'ti_trong_lam:    {ket_qua["lam_lai"] / ket_qua["tong"] * 100:.1f}%')
    print(f'he_thong / yc:   {he_thong_yc:,.0f} ({he_thong_yc / BASELINE:.2f}x)')

    print('\n=== A3 ===')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, sub)
        tl_tc = kq['thanh_cong'] / len(sub) * 100
        tb_lan = sub['so_lan_chay'].mean()
        print(f'{loai:10s} n={len(sub):3d} tc={tl_tc:5.1f}% lan={tb_lan:.2f} cps={kq["cps"]:>8,.0f} ({kq["cps"] / BASELINE:.2f}x)')
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['is_ok'] = (runs_loai['status'] == 'ok').astype(float)
    print('\nTi le ok theo attempt (%):')
    print((runs_loai.pivot_table(index='loai', columns='attempt', values='is_ok', aggfunc='mean') * 100).round(1))

    print('\n=== A4 (noi_dia + hang_nang) ===')
    sub_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, sub_pv)
    tl_tc_pv = kq_pv['thanh_cong'] / len(reqs)
    for ten_kl, kl_thang in [('45.000 yc/thang', 45000), ('Mot nua (22.500)', 22500)]:
        viec_tc_thang = kl_thang * tl_tc_pv
        co_dinh_viec = 40_000_000 / viec_tc_thang
        tong_cps = kq_pv['cps'] + co_dinh_viec
        print(f'{ten_kl:18s} tc/thang={viec_tc_thang:,.0f} co_dinh={co_dinh_viec:,.0f} tong_cps={tong_cps:,.0f} ({tong_cps / BASELINE:.2f}x)')

    print('\n=== B1 ===')
    kich_ban = {
        'Gia token gap doi':      dict(gia_vao=52, gia_ra=260),
        'Gia token giam mot nua': dict(gia_vao=13, gia_ra=65),
        'Xem lai gap doi':        dict(he_so_xem_lai=2),
        'Xem lai giam mot nua':   dict(he_so_xem_lai=0.5),
        'Lam lai gap doi':        dict(he_so_lam_lai=2),
        'Lam lai giam mot nua':   dict(he_so_lam_lai=0.5),
        'Luong tang 25%':         dict(luong_phut=2500),
        'Toi da 2 lan chay':      dict(max_lan_chay=2),
        'Chi 1 lan chay':         dict(max_lan_chay=1),
    }
    goc = ket_qua['cps']
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'{ten:24s} {cps:>8,.0f} ({(cps / goc - 1) * 100:+5.1f}%)')

    print('\n=== B2 ===')
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'Token x2 + Xem lai x2:   {cps_cap:>8,.0f} ({(cps_cap / goc - 1) * 100:+5.1f}%)')

    print('\n=== B3 ===')
    for k in [1, 2, 3]:
        kq_k = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc_k = len(reqs) - kq_k['thanh_cong']
        ca_he_thong = kq_k['tong'] + khong_tc_k * BASELINE
        print(f'Gioi han {k}: tro_ly={kq_k["tong"]:>10,.0f} khong_tc={khong_tc_k:3d} he_thong={ca_he_thong:>10,.0f} cps={kq_k["cps"]:>6,.0f}')

    print('\n=== B4 (noi_dia + hang_nang, xem lai 100%) ===')
    runs_pv = runs[runs['request_id'].isin(sub_pv['request_id'])]
    yc_co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()
    ca_lam_lai = (sub_pv['ket_qua'] == 'lam_lai').sum()
    hoa_don_pv = kq_pv['token'] + kq_pv['tool']
    xem_100 = yc_co_ok * 5 * LUONG_PHUT
    phut_ll_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for nhan, phut_ll in [('9 phut/ca (de)', 9.0), (f'{phut_ll_tb:.1f} phut/ca (data)', phut_ll_tb)]:
        tien_ll = ca_lam_lai * phut_ll * LUONG_PHUT
        tong_b4 = xem_100 + tien_ll + hoa_don_pv
        cps_b4 = tong_b4 / kq_pv['thanh_cong']
        hoa_von = (kq_pv['thanh_cong'] * BASELINE - tien_ll - hoa_don_pv) / (yc_co_ok * LUONG_PHUT)
        print(f'{nhan:22s} tong={tong_b4:>10,.0f} cps={cps_b4:>6,.0f} ({cps_b4 / BASELINE:.2f}x) hoa_von<= {hoa_von:.1f} phut')
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    def co_mau(p1, p2, alpha=0.05, power=0.8):
        za = NormalDist().inv_cdf(1 - alpha / 2)
        zb = NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    print('\n=== D1 (Co mau pilot, baseline=0.70, alpha=0.05, power=0.80, ICC=0.02) ===')
    icc = 0.02
    n_req = co_mau(0.70, 0.75)
    de_75 = 1 + (75 - 1) * icc
    n_staff_75 = math.ceil(n_req * de_75)
    so_nv_can = math.ceil(n_staff_75 / 75)
    cap_20_nv = int(20 / icc)
    cap_6_depot = int(6 / icc)
    n_mde6 = co_mau(0.70, 0.76)
    m_min_20nv = math.ceil(n_mde6 * (1 - icc) / (20 - n_mde6 * icc))
    de_mde6 = 1 + (m_min_20nv - 1) * icc
    power_5pt_at_859 = NormalIndPower().power(
        effect_size=proportion_effectsize(0.75, 0.70),
        nobs1=n_mde6,
        alpha=0.05,
        ratio=1.0,
    )
    print(f'a) Theo yeu cau (+5 diem):       {n_req:,} yc/nhom')
    print(f'b) Theo nhan vien (m=75):        DE={de_75:.2f}, n={n_staff_75:,}/nhom -> {so_nv_can} nv/nhom (tong {so_nv_can*2} > 40)')
    print(f'c) 20 nhan vien/nhom (c/ICC):    toi da {cap_20_nv:,} < {n_req:,} (khong dat 5 diem)')
    print(f'd) 6 depot/nhom (c/ICC):         toi da {cap_6_depot:,} (loai)')
    print(f'e) Muc chenh 6 diem (n={n_mde6}):   m >= {m_min_20nv} yc/nguoi, DE={de_mde6:.2f}; power neu chenh 5 diem={power_5pt_at_859:.2f}')
    yc_moi_nv_ngay = 1500 / 40
    so_ngay_toi_thieu = math.ceil(m_min_20nv / yc_moi_nv_ngay)
    print(f'   Luu luong 1.500 yc/ngay / 40 nv = {yc_moi_nv_ngay:.1f} yc/nv/ngay -> toi thieu {so_ngay_toi_thieu} ngay thu thap (+7 ngay theo doi mo lai)')

    print('\n=== D3 (Ti le mo lai trong 7 ngay hien tai) ===')
    mo_lai_all = reqs['mo_lai_trong_7_ngay'].mean()
    mo_lai_pv = sub_pv['mo_lai_trong_7_ngay'].mean()
    print(f'Toan bo (1.200 yc):      {mo_lai_all*100:.2f}% ({int(reqs["mo_lai_trong_7_ngay"].sum())}/{len(reqs)})')
    print(f'Pham vi pilot ({len(sub_pv)} yc): {mo_lai_pv*100:.2f}% ({int(sub_pv["mo_lai_trong_7_ngay"].sum())}/{len(sub_pv)})')

    print('\n=== E1 (3 chi so tren 1.200 yeu cau) ===')
    cs_chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).mean()
    xem_df = reqs[reqs['duoc_xem_lai'] == 1]
    cs_dung = xem_df['quyet_dinh_xem_lai'].isin(['sua', 'bo']).mean()
    cs_an_toan = (reqs['mo_lai_trong_7_ngay'] == 1).mean()
    print(f'Chinh (dong 24h, khong mo lai 7n): {cs_chinh*100:.2f}% ({int(((reqs["dong_trong_24h"] == 1) & (reqs["mo_lai_trong_7_ngay"] == 0)).sum())}/{len(reqs)})')
    print(f'Dung (bo qua goi y sua+bo):        {cs_dung*100:.2f}% ({int(xem_df["quyet_dinh_xem_lai"].isin(["sua", "bo"]).sum())}/{len(xem_df)})')
    print(f'An toan (mo lai trong 7 ngay):     {cs_an_toan*100:.2f}% ({int((reqs["mo_lai_trong_7_ngay"] == 1).sum())}/{len(reqs)})')
