# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ... · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn mẫu **4.472 đ** (`simulated`), gấp **16,28×** hoá đơn token+tool chia số yêu cầu (274,7 đ/yc); phạm vi pilot `noi_dia` + `hang_nang` là **3.414 đ** (cộng 40 triệu đ cố định/tháng ở 45.000 yc/tháng là **4.599 đ = 0,38×**, `simulated`). | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | **1. Số ca làm lại** (+51,8% / −25,9%) · **2. Tỉ lệ xem lại** (+40,7% / −20,3%) · **3. Lương nhân viên** (+23,1% khi tăng 25%); giờ nhân viên chiếm 92,5% tổng chi phí (`simulated`). | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | So với 12.000 đ: `noi_dia` **2.696 đ (0,22×)**, `hang_nang` **8.221 đ (0,69×)**, `doi_tac` **10.215 đ (0,85×)**, `quoc_te` **22.515 đ (1,88×)**; cả hệ thống (gồm 222 ca không thành công chuyển nhân viên × 12.000 đ) là **5.865 đ/yc (0,49×)** (`simulated`) → thu hẹp phạm vi pilot chỉ gồm `noi_dia` + `hang_nang`. | Giả lập | Giám đốc vận hành LogiX-VN |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử (chưa có đối chứng): Chính **82,83%** (994/1.200; phạm vi pilot 92,26%) · Dùng (bỏ qua gợi ý) **27,12%** (48/177; phạm vi pilot 21,09%) · An toàn (mở lại 7 ngày) **4,25%** (51/1.200; phạm vi pilot 3,97%); đã đặc tả 10 event có `trace_id`. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 5 · Bảng lỗi và cách khắc phục | 20 ca lỗi được gắn nhãn độc lập (đồng thuận ≥ 80%); lập bảng khắc phục cho 5 ca đại diện đủ 5 loại với cách phát hiện đo được (ngưỡng, tần suất) và vai trò phụ trách. | Xong, có bằng chứng | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia ngẫu nhiên theo nhân viên (20 đối chứng + 20 can thiệp phân tầng theo depot); MDE 6 điểm (859 yc/nhóm, m ≥ 299 yc/người; chấp nhận power 0,64 ở mức 5 điểm); 3 luật dừng đủ NẾU–TRONG–THÌ–KHÔNG THÌ. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại gấp đôi tăng chi phí **+51,8%** lên **6.787 đ** (`simulated`); xem lại 100% kéo dài ở `noi_dia` + `hang_nang` đẩy chi phí lên **11.743 đ = 0,98×** (hoặc **12.414 đ = 1,03×** với 15,3 phút làm lại thực tế, `simulated`); khối lượng giảm một nửa làm chi phí cố định tăng lên **+2.370 đ/việc** (tổng **5.784 đ = 0,48×**, `simulated`). | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×). Các điều kiện kèm người phụ trách và mốc kiểm tra:

- **Chống hoàn trùng và đối soát sổ cái:** Hoàn tất khoá chống trùng ghi sổ và cảnh báo lệch trạng thái trước khi mở pilot — Phụ trách: `Kỹ sư trưởng agent` · Ngày kiểm tra: trước ngày khởi chạy pilot.
- **Chốt thiết kế & đánh đổi cỡ mẫu pilot:** Ký duyệt kế hoạch chia cụm và chấp nhận mức chênh 6 điểm (power 0,64 nếu chênh thật 5 điểm) — Phụ trách: `Giám đốc vận hành LogiX-VN` · Ngày kiểm tra: trước ngày khởi chạy pilot.
- **Đo lường thật toàn bộ event:** Bật đủ 10 event có `trace_id` và thay số phút `simulated` bằng thời gian xem lại/làm lại đo thật — Phụ trách: `Kỹ sư dữ liệu` · Ngày kiểm tra: cuối tuần 1 pilot.
- **Lộ trình giảm tỉ lệ xem lại theo bậc:** Chuyển từ xem lại rộng sang xem lại chọn lọc khi `sua + bo < 15%` để tránh chi phí chạm mức 11.743–12.414 đ (`simulated`) — Phụ trách: `Trưởng nhóm CSKH` · Ngày kiểm tra: cuối bước rollout 0.25.
