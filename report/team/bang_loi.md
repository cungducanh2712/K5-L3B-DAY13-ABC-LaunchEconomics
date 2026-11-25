# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Đào Văn Hiệp (TV3) · Người gắn nhãn 2: TV4 (`htphong23`) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Hai người gắn nhãn độc lập trùng 20/20 ca (100%, không có ca bất đồng). Dưới đây là các quy tắc phân biệt theo nguyên nhân gốc được áp dụng cho các ca dễ nhầm lẫn:
- **Ca 6, 9 (`Do người dùng` thay vì `Hệ thống`):** Nguyên nhân gốc là khách chọn sai danh mục hoặc nhập sai loại mã (mã sàn TMĐT thay vì mã vận đơn); việc trợ lý chưa gợi ý chỉ là hướng cải thiện ở cột khắc phục.
- **Ca 8, 15 (`Hệ thống` thay vì `Ngầm`):** Lỗi sai so với chính sách/thiết kế nhưng đã lộ ra (trích dẫn điều khoản không tồn tại hiển thị trực tiếp cho khách, hoặc nhân viên xem lại bắt được lỗi hoàn 100% trước khi gửi), trong khi `Ngầm` chỉ dùng khi cả khách lẫn hệ thống đều không nhận ra.
- **Ca 12 (`Ngầm` thay vì `Hệ thống`):** Kết quả trả lời vẫn đúng nhưng lỗi thiếu trường ở tool depot D05 làm chi phí token đội lên gấp 3 lần suốt 3 tuần mà không ai hay cảnh báo nào nhận ra ("sai" bao gồm cả sai ngầm về chi phí vận hành).
- **Ca 13 (`Giới hạn hệ thống` thay vì `Hệ thống`):** Yêu cầu bảo hiểm hàng hóa của đối tác nằm ngoài phạm vi của trợ lý hoàn phí, nên nguyên nhân gốc là giới hạn phạm vi dù cách trợ lý từ chối/trả lời chung chung còn chưa tốt.
- **Ca 18 (`Ngữ cảnh` thay vì `Hệ thống`):** Trợ lý tính đúng số tiền hoàn 15.000 đ (50% của 30.000 đ) theo thiết kế và chính sách, chỉ có giả định "khách tự hiểu cách tính mà không cần ghi công thức" là không khớp với ngữ cảnh của khách.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm `trace_id`); cảnh báo khi vượt 2% tổng số yêu cầu mỗi ngày | Nhận diện định dạng mã đơn sàn TMĐT để tự động tra sang mã vận đơn LogiX; nếu không tra được thì hiển thị hướng dẫn kèm ảnh vị trí mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ giữa event gửi tin nhắn "đã hoàn" và `refund_ledger_write` có `ket_qua = ok` cùng `trace_id`; ngưỡng cảnh báo > 0 ca lệch | Chỉ gửi thông báo "đã hoàn tiền thành công" sau khi sổ cái trả về `ok`; nếu gặp lỗi 503 sau 3 lần thử lại thì báo khách "đang xử lý" và chuyển nhân viên (`handoff_to_staff`) | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Thống kê hàng tuần tỉ lệ `ticket_reopened` (có `trace_id`) do khiếu nại số tiền nhưng kiểm tra lại thấy tính đúng chính sách; ngưỡng > 1% số đơn hoàn 50% | Cập nhật mẫu tin nhắn hoàn tiền luôn hiển thị rõ công thức tính (ví dụ: `Phí giao 30.000 đ × 50% (trễ 24–48h) = 15.000 đ`) | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi hàng ngày tỉ lệ event `handoff_to_staff` với `reason = thieu_du_lieu` (kèm `trace_id`) tách theo từng `loai` yêu cầu; ngưỡng > 20% ở một loại | Giữ cơ chế chuyển nhân viên ngay từ lần chạy 1 kèm tóm tắt hồ sơ; loại yêu cầu `quoc_te` ra khỏi phạm vi chạy pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked` (kèm `trace_id`): kế toán kiểm tra mẫu ngẫu nhiên 100 đơn hoàn mỗi tuần đối chiếu với bảng giá hiệu lực; ngưỡng > 1% đơn lệch tiền | Tự động xóa cache bảng giá (invalidate cache) ngay khi phát hành bảng giá mới và ghi `pricing_table_version` vào `trace_id` của mỗi lần chạy | Kế toán trưởng |
