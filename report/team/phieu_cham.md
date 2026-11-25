# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ABC (L3B - H202)
- Nhóm được chấm: NhomCDE (L3B - H202)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Đề xuất **Go có điều kiện** (`noi_dia + hang_nang`, tối đa 2 lần chạy) khớp B3 (`6.901.220 đ`) và A3; nêu rõ số bất lợi là `power` còn **0,64** ở mức 5 điểm và B4 xem 100% gồm cố định lên **12.928–13.600 đ = 1,08×–1,13×** (`simulated`), kèm 4 điều kiện có vai trò và hạn `30/11/2026`. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Thu hẹp phạm vi có lý do bằng số (`noi_dia` 0,22×, `hang_nang` 0,69×; loại `quoc_te` 1,88× và `doi_tac` 0,85×) và có nhãn `simulated` ở `ho_so_launch_v0.md`, `chi_so.md`, `pilot_plan.yaml`, phần A; **tuy nhiên toàn bộ bảng B1–B4 trong `bang_chi_phi.md` thiếu nhãn `simulated`**. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên **20+20 nhân viên** phân tầng depot (`seed 20261125`), đối chứng cùng kỳ; MDE 6 điểm (`n=859`, `m ≥ 299`, `DE=6,96`); **3 luật dừng** đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ` kèm ngưỡng, thời hạn và vai trò tắt trong 30 phút (lưu ý nhỏ: `decision_date` trong YAML nên đồng bộ sang `2027-01-05`). |
| **Tổng** | | | | **25 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Nhóm đã hoàn thiện đủ 7/7 mục trên `ho_so_launch_v0.md`, `chi_so.md` (10 event có `trace_id`, 3 rủi ro E2) và trả lời đầy đủ 4 điều kiện ràng buộc trước ngày chạy; trừ 5 điểm ở tiêu chí 2 do bảng B1–B4 trong `bang_chi_phi.md` chưa gắn nhãn `simulated` trực tiếp trên các con số.

**Một câu hỏi cho đội trình:** Hiện tại trên hồ sơ launch v0 của nhóm vẫn còn 5 mục để trạng thái Chưa, file đặc tả chỉ số và event còn trống, và dòng đề xuất cuối (Go / Go có điều kiện / No-go) cũng chưa được chốt. Dựa trên những phần nhóm đã làm xong, nhóm chọn đề xuất nào cho kế hoạch pilot này và cần bổ sung điều kiện gì để hội đồng có thể duyệt?

**Câu trả lời của đội trình (ghi lại tại buổi):** Nhóm chọn đề xuất Go có điều kiện cho phạm vi thu hẹp nội địa (2.696 đ = 0,22×) và hàng nặng (8.221 đ = 0,69×) [simulated] — loại quốc tế (1,88×, thành công 27,3%) và đối tác (0,85×); sau khi cộng cố định 40 triệu đ/tháng chi phí vẫn là 4.599 đ (0,38×) ở 45.000 yêu cầu/tháng và tối ưu hệ thống ở 2 lần chạy (6.901.220 đ). Nhóm thừa nhận chưa thể mở pilot ngay khi hồ sơ còn thiếu đặc tả đo lường, và đề xuất 4 điều kiện bắt buộc hoàn tất trước ngày chạy để hội đồng duyệt: (1) Hoàn thiện đặc tả chỉ số (chính 82,83%, bỏ qua 27,12%, mở lại 4,25% toàn mẫu / 3,97% trong phạm vi), bật đủ ≥ 6 sự kiện có mã truy vết và thay toàn bộ phút giả lập (đang chiếm 92,5% chi phí) bằng số đo thật sau tuần 1 (PM trợ lý hoàn phí & Trưởng nhóm CSKH); (2) Sửa triệt để khoá chống hoàn trùng, đối soát sổ cái mỗi giờ (> 0 ca) và xoá cache bảng giá kèm kiểm tra mẫu 100 đơn/tuần (Kỹ sư trưởng trợ lý & Kế toán trưởng); (3) Giám đốc vận hành LogiX-VN ký chấp nhận đánh đổi cỡ mẫu MDE 6 điểm (20+20 nhân viên, ≥ 299 yêu cầu/người; power còn 0,64 nếu tác động thật 5 điểm) cùng quyền tắt trợ lý trong 30 phút; (4) Có lộ trình hạ tỉ lệ xem lại theo bậc xuống mức hoà vốn ≤ 4,8–5,1 phút/ca, vì nếu xem lại 100% chi phí vọt lên 11.743–12.414 đ (0,98×–1,03×) [simulated].
