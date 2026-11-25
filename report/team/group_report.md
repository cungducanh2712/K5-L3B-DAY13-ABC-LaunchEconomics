# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: ABC
- Lớp: H202 - K5 L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Xây dựng bộ **hồ sơ launch v0** (Gate 2a) cho trợ lý hoàn phí **LogiX-VN** dựa trên mẫu giả lập 1.200 yêu cầu (1.624 lần chạy) để trả lời bốn câu hỏi: (1) chi phí thật mỗi việc thành công, (2) chỉ số sử dụng và bộ event có `trace_id`, (3) phân loại lỗi và cách khắc phục theo Google PAIR, và (4) thiết kế kế hoạch pilot có nhóm đối chứng, đủ cỡ mẫu và luật dừng rõ ràng.

## 3. Giải pháp

- **Nhiệm vụ A & B (Kinh tế & Độ nhạy):** Viết mô hình `mo_hinh` trong `src/lab13.py`, vượt qua 3 phép thử A1 (`1,20 · 1,25 · 1,25`), tính chi phí theo loại yêu cầu, chi phí cố định 40 triệu đ/tháng và 9 kịch bản độ nhạy trong [bang_chi_phi.md](bang_chi_phi.md).
- **Nhiệm vụ C (Phân loại lỗi):** Hai thành viên gắn nhãn độc lập 20 ca lỗi (đồng thuận 20/20 = 100%) và lập bảng khắc phục 5 ca đại diện đủ 5 loại trong [bang_loi.md](bang_loi.md).
- **Nhiệm vụ D (Kế hoạch pilot):** Tính cỡ mẫu cụm (`co_mau` + `statsmodels`), chọn chia ngẫu nhiên theo nhân viên (20 đối chứng + 20 can thiệp, mở dần `4 → 10 → 20`), chấp nhận MDE 6 điểm và soạn 3 luật dừng đủ 4 vế trong [pilot_plan.yaml](pilot_plan.yaml).
- **Nhiệm vụ E (Chỉ số, rủi ro & Hồ sơ v0):** Đặc tả 5 chỉ số, 10 event có `trace_id`, 3 dòng rủi ro kinh tế trong [chi_so.md](chi_so.md) và tổng hợp thành một trang đề xuất trong [ho_so_launch_v0.md](ho_so_launch_v0.md).

## 4. Kết quả

- **Chi phí mỗi việc thành công:** Toàn mẫu **4.472 đ** (`simulated`, gấp 16,3× hoá đơn token+tool/yêu cầu); phạm vi pilot `noi_dia` + `hang_nang` là **3.414 đ** (cộng cố định 40 triệu đ/tháng ở 45.000 yc/tháng là **4.599 đ = 0,38×**, `simulated`).
- **Yếu tố nhạy nhất:** 1. Số ca làm lại (+51,8% / -25,9%) · 2. Tỉ lệ xem lại (+40,7% / -20,3%) · 3. Lương nhân viên (+23,1%). Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (**6.901.220 đ**, `simulated`).
- **Chỉ số đợt chạy thử (chưa có đối chứng):** Chính **82,83%**, bỏ qua gợi ý **27,12%**, mở lại 7 ngày **4,25%**.
- **Đề xuất Gate 2a:** **Go có điều kiện** cho pilot phạm vi `noi_dia` + `hang_nang` (loại `quoc_te` 1,88× và `doi_tac` 0,85×).
- **Kết quả duyệt chéo từ hội đồng:** *(cập nhật sau phiên duyệt chéo 17:00–17:45)*.

## 5. Khó khăn và cách xử lý

- **Khác biệt logic khi giới hạn số lần chạy & tính B4:** Khi tích hợp code từ nhánh `tv1-economics` vào `src/lab13.py`, nhóm phát hiện thiếu bước đặt lại phút xem lại/làm lại về `0` cho các ca vượt `max_lan_chay` và cách tính B4 chưa tách 2 mức 9 phút vs 15,3 phút/ca; đã chuẩn hóa lại để khớp đáp án và rubric.
- **Giới hạn cỡ mẫu với 40 nhân viên:** Không cách chia cụm nào đạt mức chênh 5 điểm ở power 0,80; nhóm ghi nhận rõ đánh đổi sang MDE 6 điểm (`n = 859`/nhóm, `m ≥ 299`, thu thập tối thiểu 8 ngày, power còn `0,64` ở mức 5 điểm).

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Thời gian xem lại/làm lại hiện dựa trên cột `_simulated`; cần bật đủ 10 event có `trace_id` để thay bằng số đo thật sau tuần 1 pilot.
- Cần triển khai khóa chống trùng và đối soát sổ cái tự động trước khi mở pilot để ngăn lỗi hoàn trùng.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models* (`arxiv.org/abs/2504.13359`).
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure".
- Tài liệu `statsmodels` (`stats.power.NormalIndPower`).
