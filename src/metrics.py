"""Lab 13 · Nhiệm vụ E1, E2 — Đặc tả chỉ số, event và rủi ro kinh tế (TV4).

Chạy độc lập trong thư mục src/ hoặc từ root repo:
    python3 metrics.py
"""
import csv
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    pd = None


PHAM_VI_PILOT = {'noi_dia', 'hang_nang'}

DANH_SACH_EVENT = [
    {
        'event': 'refund_request_created',
        'ai_tao': 'App khách',
        'thuoc_tinh': 'request_id, loai, so_tien, arm, trace_id',
        'thoi_diem': 'Khi khách gửi yêu cầu hoàn phí',
    },
    {
        'event': 'agent_run_completed',
        'ai_tao': 'Agent',
        'thuoc_tinh': 'attempt, tokens_in, tokens_out, tool_calls, status, trace_id',
        'thoi_diem': 'Sau mỗi lần chạy, kể cả lần lỗi',
    },
    {
        'event': 'agent_suggestion_shown',
        'ai_tao': 'Giao diện nhân viên',
        'thuoc_tinh': 'staff_id, so_tien_de_xuat, trace_id',
        'thoi_diem': 'Khi gợi ý trợ lý hiện ra cho nhân viên',
    },
    {
        'event': 'staff_review_decision',
        'ai_tao': 'Nhân viên',
        'thuoc_tinh': 'quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id',
        'thoi_diem': 'Khi nhân viên bấm giữ, sửa hoặc bỏ gợi ý',
    },
    {
        'event': 'staff_rework_completed',
        'ai_tao': 'Nhân viên',
        'thuoc_tinh': 'phut_lam_lai (đo thật), ly_do, trace_id',
        'thoi_diem': 'Khi nhân viên làm lại xong ca lỗi',
    },
    {
        'event': 'refund_ledger_write',
        'ai_tao': 'Dịch vụ sổ cái',
        'thuoc_tinh': 'idempotency_key, so_tien, ket_qua, trace_id',
        'thoi_diem': 'Khi ghi giao dịch hoàn tiền vào sổ cái',
    },
    {
        'event': 'handoff_to_staff',
        'ai_tao': 'Agent',
        'thuoc_tinh': 'reason, tom_tat, trace_id',
        'thoi_diem': 'Khi chuyển yêu cầu sang nhân viên xử lý',
    },
    {
        'event': 'ticket_closed',
        'ai_tao': 'Hệ thống ticket',
        'thuoc_tinh': 'closed_at, trace_id',
        'thoi_diem': 'Khi yêu cầu hoàn phí được đóng',
    },
    {
        'event': 'ticket_reopened',
        'ai_tao': 'Khách',
        'thuoc_tinh': 'reopened_at, reason, trace_id',
        'thoi_diem': 'Khi khách mở lại yêu cầu trong 7 ngày',
    },
    {
        'event': 'audit_sample_checked',
        'ai_tao': 'Kế toán',
        'thuoc_tinh': 'so_tien_da_hoan, so_tien_dung, trace_id',
        'thoi_diem': 'Kiểm tra mẫu ngẫu nhiên hằng tuần',
    },
]

RUI_RO_KINH_TE = [
    {
        'rui_ro': 'Số ca làm lại tăng gấp đôi',
        'tac_dong': (
            'Chi phí mỗi việc thành công tăng +51,8%, từ 4.472 đ lên 6.787 đ '
            '(simulated)'
        ),
        'dau_hieu': (
            'Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử trong phạm vi '
            'noi_dia + hang_nang là 4,89%, 48/982)'
        ),
        'hanh_dong': 'Thu hẹp về noi_dia và rà soát 20 trace có ket_qua = lam_lai',
        'phu_trach': 'PM trợ lý hoàn phí',
    },
    {
        'rui_ro': 'Phải xem lại 100% kéo dài',
        'tac_dong': (
            'Trong phạm vi noi_dia + hang_nang, chi phí lên 11.743 đ = 0,98× '
            '(simulated, 9 phút làm lại) hoặc 12.414 đ = 1,03× (simulated, '
            '15,3 phút làm lại thực tế), mất lợi thế so với 12.000 đ'
        ),
        'dau_hieu': (
            'Tỉ lệ yêu cầu được xem lại > 50% ở cuối bước rollout 0.25 hoặc '
            'thời gian xem lại trung bình > 4,8–5,1 phút'
        ),
        'hanh_dong': (
            'Giảm tỉ lệ xem lại theo bậc khi tỉ lệ sửa + bỏ < 15% và tinh gọn '
            'màn hình kiểm tra'
        ),
        'phu_trach': 'Trưởng nhóm CSKH',
    },
    {
        'rui_ro': 'Khối lượng yêu cầu thấp hơn dự kiến',
        'tac_dong': (
            'Chi phí cố định 40 triệu đ/tháng tăng từ +1.185 đ/việc (4.599 đ '
            '= 0,38× ở 45.000 yc/tháng, simulated) lên +2.370 đ/việc khi còn '
            'một nửa (5.784 đ = 0,48×, simulated)'
        ),
        'dau_hieu': 'Số việc thành công theo tuần < 50% kế hoạch dự kiến',
        'hanh_dong': 'Không mở rộng phạm vi pilot và đàm phán lại chi phí cố định',
        'phu_trach': 'PM trợ lý hoàn phí',
    },
]


def _tim_file_du_lieu(path):
    """Tìm file CSV từ thư mục hiện tại, src/ hoặc thư mục chứa module."""
    p = Path(path)
    ung_vien = [
        p,
        Path('src') / p,
        Path(__file__).resolve().parent / p.name,
    ]
    for candidate in ung_vien:
        if candidate.is_file():
            return candidate
    raise FileNotFoundError(f'Không tìm thấy file dữ liệu: {path}')


def doc_requests(path='logix_requests.csv'):
    """Đọc dữ liệu logix_requests.csv với keep_default_na=False (fallback csv chuẩn)."""
    file_path = _tim_file_du_lieu(path)
    if pd is not None:
        return pd.read_csv(file_path, keep_default_na=False)
    with open(file_path, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))


def _chuan_hoa_rows(reqs):
    """Chuyển DataFrame hoặc danh sách dict về dạng danh sách dict thống nhất."""
    if pd is not None and isinstance(reqs, pd.DataFrame):
        return reqs.to_dict('records')
    return list(reqs)


def _la_mot(gia_tri):
    """Kiểm tra giá trị cờ nhị phân bằng 1 (hỗ trợ cả int và str)."""
    return int(gia_tri) == 1


def _tinh_chi_so_nhom(rows):
    """Tính ba chỉ số (chính, dùng, an toàn) cho một tập yêu cầu."""
    tong = len(rows)
    if tong == 0:
        return {
            'tong_yeu_cau': 0,
            'chinh_tu': 0,
            'chinh_mau': 0,
            'chinh_ti_le': 0.0,
            'dung_tu': 0,
            'dung_mau': 0,
            'dung_ti_le': 0.0,
            'an_toan_tu': 0,
            'an_toan_mau': 0,
            'an_toan_ti_le': 0.0,
        }

    chinh_tu = sum(
        1
        for r in rows
        if _la_mot(r['dong_trong_24h']) and not _la_mot(r['mo_lai_trong_7_ngay'])
    )
    xem_lai_rows = [r for r in rows if _la_mot(r['duoc_xem_lai'])]
    dung_mau = len(xem_lai_rows)
    dung_tu = sum(
        1
        for r in xem_lai_rows
        if str(r.get('quyet_dinh_xem_lai', '')).strip() in {'sua', 'bo'}
    )
    an_toan_tu = sum(1 for r in rows if _la_mot(r['mo_lai_trong_7_ngay']))

    return {
        'tong_yeu_cau': tong,
        'chinh_tu': chinh_tu,
        'chinh_mau': tong,
        'chinh_ti_le': chinh_tu / tong,
        'dung_tu': dung_tu,
        'dung_mau': dung_mau,
        'dung_ti_le': (dung_tu / dung_mau) if dung_mau else 0.0,
        'an_toan_tu': an_toan_tu,
        'an_toan_mau': tong,
        'an_toan_ti_le': an_toan_tu / tong,
    }


def tinh_chi_so(reqs):
    """Tính ba chỉ số trên toàn mẫu và trong phạm vi pilot (noi_dia + hang_nang)."""
    rows = _chuan_hoa_rows(reqs)
    pilot_rows = [r for r in rows if r.get('loai') in PHAM_VI_PILOT]
    return {
        'toan_mau': _tinh_chi_so_nhom(rows),
        'pham_vi_pilot': _tinh_chi_so_nhom(pilot_rows),
    }


def _dinh_dang_phan_tram(ti_le, tu, mau):
    """Định dạng phần trăm theo dấu phẩy tiếng Việt kèm tử/mẫu."""
    return f'{ti_le * 100:.2f}% ({tu}/{mau})'.replace('.', ',')


def in_bao_cao_chi_so(reqs=None):
    """In kết quả tính chỉ số E1, kiểm tra event và tóm tắt rủi ro kinh tế E2."""
    if reqs is None:
        reqs = doc_requests()
    kq = tinh_chi_so(reqs)
    tm = kq['toan_mau']
    pv = kq['pham_vi_pilot']

    print('=== Nhiệm vụ E1 · Ba chỉ số trong đợt chạy thử (không có đối chứng) ===')
    print(f"Toàn mẫu ({tm['tong_yeu_cau']} yêu cầu):")
    print(f"  - Chỉ số chính (đóng 24h, không mở lại 7 ngày): {_dinh_dang_phan_tram(tm['chinh_ti_le'], tm['chinh_tu'], tm['chinh_mau'])}")
    print(f"  - Chỉ số dùng (tỉ lệ bỏ qua gợi ý sua + bo):    {_dinh_dang_phan_tram(tm['dung_ti_le'], tm['dung_tu'], tm['dung_mau'])}")
    print(f"  - Chỉ số an toàn (tỉ lệ mở lại trong 7 ngày):  {_dinh_dang_phan_tram(tm['an_toan_ti_le'], tm['an_toan_tu'], tm['an_toan_mau'])}")
    print(f"Phạm vi pilot noi_dia + hang_nang ({pv['tong_yeu_cau']} yêu cầu):")
    print(f"  - Chỉ số chính:   {_dinh_dang_phan_tram(pv['chinh_ti_le'], pv['chinh_tu'], pv['chinh_mau'])}")
    print(f"  - Chỉ số dùng:    {_dinh_dang_phan_tram(pv['dung_ti_le'], pv['dung_tu'], pv['dung_mau'])}")
    print(f"  - Chỉ số an toàn: {_dinh_dang_phan_tram(pv['an_toan_ti_le'], pv['an_toan_tu'], pv['an_toan_mau'])}")
    print(f'\nSố event đã đặc tả (đều có trace_id): {len(DANH_SACH_EVENT)}')
    print(f'Số dòng rủi ro kinh tế (simulated):    {len(RUI_RO_KINH_TE)}')


if __name__ == '__main__':
    in_bao_cao_chi_so()
