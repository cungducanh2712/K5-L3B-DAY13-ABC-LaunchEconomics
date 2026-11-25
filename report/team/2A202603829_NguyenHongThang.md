# Báo cáo cá nhân — NguyenHongThang-2A202603829

## 1. Thông tin thành viên

- Họ tên: Nguyễn Hồng Thắng
- MSSV: 2A202603829
- Email: (cập nhật nếu cần)
- Vai trong nhóm: Thành viên 1 (TV1) — Người viết code (CP1–CP2: Chi phí và độ nhạy)

## 2. Phần việc phụ trách

- Phụ trách toàn bộ **CP1–CP2 (Nhiệm vụ A1–A4 và B1–B4)** trên nhánh `tv1-economics`.
- Chạy 3 kiểm thử đáp án biết trước (A1), xây dựng mô hình chi phí từ trace (A2–A4), phân tích độ nhạy (B1–B4).
- Bàn giao `src/economics.py`, `report/team/bang_chi_phi.md` và gửi kết quả theo loại yêu cầu + bảng độ nhạy cho TV2, TV4.

## 3. Đóng góp cụ thể

- Cài đặt các hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`, `kiem_tra_dap_an_biet_truoc` và `mo_hinh` trong `src/economics.py`.
- Tính toán chi phí từ `logix_runs.csv` và `logix_requests.csv`: tổng chi phí 4.373.585 đ (`simulated`), chi phí mỗi việc thành công 4.472 đ (`simulated`), gấp 16,28 lần hóa đơn token+tool chia số yêu cầu (275 đ).
- Tách chi phí theo 4 loại yêu cầu (`noi_dia` 2.696 đ, `hang_nang` 8.221 đ, `doi_tac` 10.215 đ, `quoc_te` 22.515 đ — không đáng xử lý) và tính chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`.
- Chạy 9 kịch bản độ nhạy (B1), kịch bản kết hợp (B2), giới hạn chạy lại 1–3 lần (B3) và kịch bản xem lại 100% (B4: 12.962 đ/việc, `simulated`).

## 4. Bằng chứng

- Nhánh làm việc: `tv1-economics` (đã merge vào `main`).
- Commit: `73b6108` (`TV1: hoan thanh mo hinh chi phi va do nhay (CP1-CP2)`).
- File bàn giao:
  - `src/economics.py`
  - `report/team/bang_chi_phi.md`
  - `report/team/2A202603829_NguyenHongThang.md`

## 5. Công cụ AI đã dùng

- Công cụ: Antigravity (trợ lý AI trong IDE).
- Mục đích: Hỗ trợ viết code `src/economics.py`, kiểm tra công thức A1–A4, B1–B4 và đối chiếu checklist `CHECKPOINTS.md`, `RULES.md`, `RUBRIC.md`.
- Cách tự kiểm tra: Chạy trực tiếp `python economics.py` trong `src/` để xác nhận 3 phép thử A1 đạt (`1,2000`, `1,2500`, `1,2500`), đối chiếu tính đối xứng của các kịch bản giảm một nửa / gấp đôi ở B1, và kiểm tra nhãn `simulated` cho mọi số tính từ cột `_simulated`.

## 6. Tự đánh giá

- Hoàn thành 100% phạm vi công việc của TV1 (CP1–CP2) đúng hạn, không chỉnh sửa dữ liệu gốc hay phần việc của thành viên khác.
