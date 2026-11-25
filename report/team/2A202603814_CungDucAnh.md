# Báo cáo cá nhân — CungDucAnh-2A202603814

## 1. Thông tin thành viên

- Họ tên: Cung Đức Anh
- MSSV: 2A202603814
- Email: 26ai.anhcd2@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số (nửa đầu CP1–CP2) -> Đổi sang Người viết code (nửa sau CP4–CP5)

## 2. Phần việc phụ trách

- **CP1–CP2 (Người kiểm số):** Đối chiếu mô hình chi phí A1–A4 và bảng độ nhạy B1–B4 sau khi merge nhánh `tv1-economics`; kiểm tra nhãn `simulated` và chuẩn hóa kết quả vào `src/lab13.py` và `report/team/bang_chi_phi.md`.
- **CP4–CP5 (Người viết code):** Viết code tính cỡ mẫu D1 (kèm kiểm tra power với `statsmodels`), tỉ lệ mở lại D3, và 3 chỉ số E1 trong `src/lab13.py`; hoàn thiện `report/team/pilot_plan.yaml` và `report/team/chi_so.md`.

## 3. Đóng góp cụ thể

- Phát hiện và sửa 3 sai lệch từ nhánh `tv1-economics`: đưa toàn bộ code vào đúng file nộp `src/lab13.py`, sửa lỗi quên reset `phut_xem_lai_simulated` / `phut_lam_lai_simulated` về `0` khi giới hạn `max_lan_chay` (giúp B3 ra đúng giới hạn 2 lần rẻ nhất `6.901.220 đ`), và chuẩn hóa B4 cho cả 2 mức 9 phút và 15,3 phút/ca.
- Triển khai D1 (ra đúng `1.251`, `3.103`, `1.000`, `300`, `859`, `m >= 299`, power `0,64` ở mức 5 điểm), D3 (`4,25%` toàn bộ; `3,97%` phạm vi pilot), và E1 (`82,83%`, `27,12%`, `4,25%`).
- Điền hoàn chỉnh `report/team/pilot_plan.yaml` (3 luật dừng đủ 4 vế `NẾU – TRONG – THÌ – KHÔNG THÌ`, `identifiability`, `simulated_inputs`) và `report/team/chi_so.md` (bảng E1, 10 event có `trace_id`, 3 dòng rủi ro kinh tế E2).

## 4. Bằng chứng

- Nhánh `DucAnh`: commit `5f224f0` (CP1–CP2), commit `818eef3` (CP4–E1) và commit hoàn thiện hồ sơ cá nhân + `chi_so.md`.
- Chạy `.\.venv\Scripts\python.exe lab13.py` trong `src/` in `Ba phép thử đáp án biết trước: ĐẠT` (`1.20`, `1.25`, `1.25`) và kiểm tra `yaml.safe_load` trên `report/team/pilot_plan.yaml` thành công, không còn dấu `?`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI trong IDE (Antigravity).
- **Mục đích sử dụng:** Giải thích công thức cỡ mẫu cụm (DE, ICC), gợi ý viết code cho `src/lab13.py`, soát lỗi logic khi giới hạn `max_lan_chay`, và rà soát checklist/rubric trước khi commit.
- **Cách tự kiểm tra:** Tự đối chiếu từng con số đầu ra của `src/lab13.py` với tài liệu `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (sai số 0%), kiểm tra tay công thức A1/A2/B3, và chạy kiểm tra `yaml.safe_load` + tìm từ cấm `"production"`.

## 6. Tự đánh giá

- Hoàn thành đúng vai trò kép (kiểm số nửa đầu + viết code nửa sau), kịp mốc để nhóm tổng hợp hồ sơ launch v0 trước 17:00 và sẵn sàng giải thích số liệu trước hội đồng Gate 2a.
