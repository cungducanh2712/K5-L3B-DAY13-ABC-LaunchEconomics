# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)** *(phạm vi `noi_dia` + `hang_nang`: 92,26%, 906/982)* |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại (`duoc_xem_lai == 1`) | **27,12% (48/177)** *(phạm vi `noi_dia` + `hang_nang`: 21,09%, 27/128)* |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** *(phạm vi `noi_dia` + `hang_nang`: 3,97%, 39/982)* |
| Dùng | Nhóm tự đề xuất: Tỉ lệ yêu cầu nhóm can thiệp mở xem gợi ý trợ lý | Số yêu cầu có `agent_suggestion_shown` chia số `refund_request_created` ở `arm = treatment` | Không cần tính |
| An toàn | Nhóm tự đề xuất: Tỉ lệ đơn hoàn sai số tiền hoặc sai chính sách qua kiểm tra mẫu hằng tuần | Số ca có `so_tien_da_hoan != so_tien_dung` chia tổng số ca `audit_sample_checked` (bắt lỗi ngầm như ca 5, 17) | Không cần tính |

**Lưu ý diễn giải:** Chỉ số trong đợt chạy thử là **82,83%** trên toàn mẫu (**92,26%** trong phạm vi `noi_dia` + `hang_nang`), **không** viết "trợ lý đã nâng chỉ số" vì đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event cốt lõi cần ghi nhận trong giai đoạn pilot, mỗi event đều có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id, loai, so_tien, arm, trace_id` | Khi khách gửi yêu cầu hoàn phí |
| `agent_run_completed` | Agent | `attempt, tokens_in, tokens_out, tool_calls, status, trace_id` | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | `staff_id, so_tien_de_xuat, trace_id` | Khi gợi ý của trợ lý hiện ra |
| `staff_review_decision` | Nhân viên | `quyet_dinh (giu/sua/bo), phut_xem_lai (đo thật), trace_id` | Khi nhân viên bấm giữ, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai (đo thật), ly_do, trace_id` | Khi nhân viên làm lại xong ca lỗi |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key, so_tien, ket_qua, trace_id` | Khi ghi giao dịch hoàn tiền vào sổ cái |
| `handoff_to_staff` | Agent | `reason, tom_tat, trace_id` | Khi chuyển yêu cầu sang nhân viên |
| `ticket_closed` | Hệ thống ticket | `closed_at, trace_id` | Khi đóng yêu cầu hoàn phí |
| `ticket_reopened` | Khách | `reopened_at, reason, trace_id` | Khi khách mở lại yêu cầu trong 7 ngày |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan, so_tien_dung, trace_id` | Kiểm tra mẫu ngẫu nhiên hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chỉ số chính (% đóng trong 24h và không mở lại 7 ngày):** Nối theo `trace_id` giữa `refund_request_created`, `ticket_closed` (`closed_at - created_at <= 24h`) và không phát sinh `ticket_reopened` trong 7 ngày → **đo được**.
- **Chỉ số dùng (Tỉ lệ bỏ qua gợi ý):** Đếm `staff_review_decision` có `quyet_dinh` thuộc `{sua, bo}` chia tổng số `agent_suggestion_shown` (nối theo `trace_id`) → **đo được**.
- **Chỉ số an toàn (Tỉ lệ lỗi lọt đến khách):** Đếm `ticket_reopened` trong 7 ngày chia tổng `refund_request_created` (nối theo `trace_id`) → **đo được**.
- **Chỉ số dùng tự đề xuất (% mở xem trợ lý ở nhóm can thiệp):** Đếm `agent_suggestion_shown` chia `refund_request_created` lọc theo `arm = treatment` (nối theo `trace_id`) → **đo được**.
- **Chỉ số an toàn tự đề xuất (% hoàn sai tiền qua kiểm tra mẫu):** Đếm `audit_sample_checked` có `so_tien_da_hoan != so_tien_dung` chia tổng số `audit_sample_checked` → **đo được**.

## E2 · Rủi ro kinh tế

Ba rủi ro lấy số trực tiếp từ bảng độ nhạy CP2 (`bang_chi_phi.md`). Mọi con số tính từ hai cột `_simulated` đều có nhãn `simulated`.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **+51,8%**, từ **4.472 đ** lên **6.787 đ** (`simulated`) | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử trong `noi_dia` + `hang_nang` là 4,89%, 48/982) | Thu hẹp phạm vi về `noi_dia` và rà soát 20 trace có `ket_qua = lam_lai` | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | Trong `noi_dia` + `hang_nang`, chi phí lên **11.743 đ = 0,98×** (`simulated`, với 9 phút làm lại) hoặc **12.414 đ = 1,03×** (`simulated`, với 15,3 phút làm lại thực tế), mất lợi thế so với 12.000 đ | Tỉ lệ yêu cầu được xem lại > 50% ở cuối bước rollout 0.25 hoặc thời gian xem lại trung bình > 4,8–5,1 phút | Giảm tỉ lệ xem lại theo bậc khi tỉ lệ `sua + bo` < 15% và tinh gọn màn hình kiểm tra | Trưởng nhóm CSKH |
| Khối lượng yêu cầu thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tăng từ **+1.185 đ/việc** (tổng **4.599 đ = 0,38×** ở 45.000 yc/tháng, `simulated`) lên **+2.370 đ/việc** khi còn một nửa (tổng **5.784 đ = 0,48×**, `simulated`) | Số việc thành công theo tuần < 50% kế hoạch dự kiến | Không mở rộng phạm vi pilot và đàm phán lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
