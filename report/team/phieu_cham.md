# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): ABC (L3B - H202)
- Nhóm được chấm: NhomCDE (L3B - H202)

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 0 | Trên `ho_so_launch_v0.md`, nhóm **chưa chọn đề xuất** (giữ nguyên mẫu `Go · Go có điều kiện · No-go`); **5/7 mục** (Mục 2, 4, 5, 6, 7) còn để trạng thái `Chưa`; `chi_so.md` còn trống. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 5 | Có thu hẹp phạm vi về `noi_dia + hang_nang` (loại `quoc_te` 1,88×, `doi_tac` 0,85×) và có nhãn `simulated` ở phần A, `pilot_plan.yaml`; tuy nhiên **toàn bộ phần B1–B4** trong `bang_chi_phi.md` **thiếu nhãn `simulated`**. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 5 | `pilot_plan.yaml` đọc được bằng `yaml.safe_load`, không còn `?`, có đối chứng `20+20 nhân viên`, `MDE = 0.06` (`n=859`, `DE=6.96`) và 3 luật dừng đủ 4 vế `NẾU–TRONG–THÌ–KHÔNG THÌ`. Tuy nhiên Mục 6 trên `ho_so_launch_v0.md` vẫn ghi `Chưa`, chú thích D2 để trống và `decision_date: 2026-11-25` đặt ngay ngày lab. |
| **Tổng** | | | | **10 / 30** | |

**Quyết định của hội đồng:** No-go

**Lý do:** Hồ sơ launch v0 chưa hoàn thiện (5/7 mục để trạng thái `Chưa`, chưa chọn đề xuất cuối, `chi_so.md` còn trống). Để quay lại cổng Gate 2a, nhóm cần hoàn thiện `chi_so.md`, điền đủ 7 mục + đề xuất vào `ho_so_launch_v0.md` (nêu rõ số bất lợi từ B4: `11.743–12.414 đ`), bổ sung nhãn `simulated` cho B1–B4 trong `bang_chi_phi.md` và cập nhật `decision_date` phù hợp với lịch rollout.

**Một câu hỏi cho đội trình:** Hiện tại trên hồ sơ launch v0 của nhóm vẫn còn 5 mục để trạng thái Chưa, file đặc tả chỉ số và event còn trống, và dòng đề xuất cuối (Go / Go có điều kiện / No-go) cũng chưa được chốt. Dựa trên những phần nhóm đã làm xong, nhóm chọn đề xuất nào cho kế hoạch pilot này và cần bổ sung điều kiện gì để hội đồng có thể duyệt?

**Câu trả lời của đội trình (ghi lại tại buổi):** ...
