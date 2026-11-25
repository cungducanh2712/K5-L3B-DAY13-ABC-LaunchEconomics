# Báo cáo cá nhân — HoangThePhong-2A202603832

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

## 1. Thông tin thành viên

- Họ tên: Hoàng Thế Phong
- MSSV: 2A202603832
- Email: phonghoangthe112@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ (TV4 — Chỉ số, Hồ sơ và Tích hợp · CP5)

## 2. Phần việc phụ trách

- Phụ trách chính Nhiệm vụ E (CP5 — Chỉ số, event, rủi ro kinh tế và Hồ sơ launch v0 Gate 2a).
- Đảm nhiệm vai trò Người gắn nhãn 2 tại Nhiệm vụ C (CP3): phân loại độc lập 20 ca lỗi theo khung Google PAIR (**Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**) theo nguyên nhân gốc, đối chiếu cùng Người gắn nhãn 1 (TV3).
- Đảm nhiệm vai trò Tích hợp (Integrator): kéo các nhánh `tv1-economics`, `tv3-reliability`, `DucAnh` về nhánh `tv4-launch`, giải quyết xung đột merge, đối chiếu số liệu và rà soát các quy tắc kiểm tra (không từ cấm, nhãn `simulated`, không dấu `?` trong yaml).
- Xây dựng và hoàn thiện hồ sơ launch v0 một trang [report/team/ho_so_launch_v0.md](ho_so_launch_v0.md) và đặc tả chỉ số [report/team/chi_so.md](chi_so.md).

## 3. Đóng góp cụ thể

- **Nhiệm vụ E1 (Chỉ số và event):**
  - Viết code tính toán và kiểm tra 3 chỉ số từ `src/logix_requests.csv` (với `keep_default_na=False`):
    - Chỉ số chính (% đóng 24h và không mở lại trong 7 ngày): **82,83%** (994/1.200) trên toàn mẫu và **92,26%** (906/982) trong phạm vi pilot `noi_dia` + `hang_nang`.
    - Chỉ số dùng (tỉ lệ bỏ qua gợi ý `sua` + `bo`): **27,12%** (48/177) trên toàn mẫu và **21,09%** (27/128) trong phạm vi pilot.
    - Chỉ số an toàn (tỉ lệ mở lại trong 7 ngày): **4,25%** (51/1.200) trên toàn mẫu và **3,97%** (39/982) trong phạm vi pilot.
  - Tuân thủ quy định diễn giải: Ghi rõ "chỉ số trong đợt chạy thử là...", không ghi "trợ lý đã nâng chỉ số" do chạy thử chưa có đối chứng.
  - Đề xuất thêm 2 chỉ số mới (Chỉ số dùng: % yêu cầu nhóm can thiệp được mở xem gợi ý trợ lý; Chỉ số an toàn: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần).
  - Đặc tả danh sách 10 event có `trace_id` và kiểm tra chéo 100% các chỉ số đều đo được từ log event.
- **Nhiệm vụ E2 (Rủi ro kinh tế):**
  - Lấy số liệu từ bảng độ nhạy CP2 để lập 3 kịch bản rủi ro: Làm lại x2 (+51,8% lên 6.787 đ, `simulated`), Xem lại 100% kéo dài (11.743 đ = 0,98× hoặc 12.414 đ = 1,03×, `simulated`), Khối lượng thấp hơn dự kiến (chi phí cố định 40tr/tháng tăng lên +2.370 đ/việc, tổng 5.784 đ = 0,48×, `simulated`). Gán người phụ trách là một vai trò cụ thể.
- **Nhiệm vụ C (Gắn nhãn lỗi độc lập):**
  - Gắn nhãn độc lập 20 ca lỗi vào cột `Nhãn người 2` trong `bang_loi.md`, đối chiếu cùng TV3 đạt đồng thuận tuyệt đối 20/20 ca (100%).
- **Nhiệm vụ E3 (Hồ sơ Launch v0):**
  - Khởi tạo và hoàn thiện file `ho_so_launch_v0.md` đúng 1 trang, đủ 7 mục, chuẩn hóa trạng thái (`Giả lập` / `Xong, có bằng chứng`), người phụ trách cụ thể và đề xuất **Go có điều kiện** cho phạm vi `noi_dia` + `hang_nang` kèm 4 điều kiện rõ ràng.
- **Tích hợp và kiểm thử repo:**
  - Merge thành công toàn bộ đóng góp của TV1, TV2, TV3 vào nhánh `tv4-launch`.
  - Tự động kiểm tra: sạch 100% dấu `?` trong `pilot_plan.yaml`, sạch 100% từ cấm trong toàn bộ thư mục `report/team/` và `src/`.

## 4. Bằng chứng

- Code và dữ liệu: `src/metrics.py`, `src/lab13.py`.
- Báo cáo và hồ sơ: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`.
- Các commit trên Git nhánh `tv4-launch`:
  - `223736b`: *TV4: hoan thanh dac ta chi so (E1, E2), khoi tao ho so launch v0 va nhan 20 ca loi (Nguoi 2)*
  - `852b0e4`: *Merge branch 'origin/tv3-reliability' into tv4-launch: hoan thanh bang_loi CP3*
  - `f009196`: *Merge branch 'origin/DucAnh' into tv4-launch: tich hop CP4 pilot_plan va lab13.py*
  - `6986b06`: *TV4: chuan hoa tu ngu tranh grep tu cam trong bao cao TV3*

## 5. Công cụ AI và cách tự kiểm tra

- **Công cụ AI đã sử dụng:** Cursor / Claude / Antigravity Agent để hỗ trợ soát lỗi cú pháp Markdown, regex kiểm tra định dạng và cấu trúc dữ liệu bảng.
- **Cách tự kiểm tra và liêm chính:**
  - Tự tay viết script và đối soát dữ liệu với hai file CSV (`logix_requests.csv`, `logix_runs.csv`) bằng Python.
  - Chạy lệnh kiểm tra không có từ cấm (chỉ dùng pilot/chạy thử, không dùng từ cấm môi trường chính thức).
  - Kiểm tra tính hợp lệ của YAML: `python3 -c "import yaml; yaml.safe_load(open('report/team/pilot_plan.yaml'))"`.
  - Kiểm tra nhãn `simulated` ở tất cả các con số liên quan đến số phút giả lập.
