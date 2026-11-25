# Báo cáo cá nhân — DaoVanHiep-2A202603813

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

## 1. Thông tin thành viên

- Họ tên: Đào Văn Hiệp
- MSSV: 2A202603813
- Email: 26ai.hiepdv3@vinuni.edu.vn
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 1 (TV3 — Phân tích lỗi · CP3)

## 2. Phần việc phụ trách

- Phụ trách Nhiệm vụ C (CP3 — Phân tích lỗi và cách khắc phục) trên nhánh `tv3-reliability`.
- Đọc đề bài 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, áp dụng khung phân loại 5 nhóm lỗi của Google PAIR (**Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**) theo nguyên nhân gốc.
- Gắn nhãn độc lập đủ 20 ca lỗi (cột `Nhãn người 1`), sau đó đối chiếu với bộ nhãn độc lập của TV4 (`Nhãn người 2`), tính tỉ lệ đồng thuận và ghi quy tắc phân biệt cho các ca dễ nhầm/bất đồng.
- Thiết kế bảng khắc phục cho 5 ca đại diện (mỗi loại 1 ca) với cách phát hiện đo được (event có `trace_id`, ngưỡng cảnh báo, tần suất) và gắn đúng 1 vai trò phụ trách có quyền quyết định.

## 3. Đóng góp cụ thể

- Hoàn thành bộ nhãn độc lập 20 ca lỗi ở cột `Nhãn người 1` trong `report/team/bang_loi.md`:
  - **Do người dùng (4 ca):** Ca 1, 6, 9, 14.
  - **Hệ thống (5 ca):** Ca 2, 7, 8, 15, 20.
  - **Ngữ cảnh (4 ca):** Ca 3, 10, 16, 18.
  - **Giới hạn hệ thống (4 ca):** Ca 4, 11, 13, 19.
  - **Ngầm (3 ca):** Ca 5, 12, 17.
- Xây dựng bảng khắc phục 5 ca đại diện (Ca 9, Ca 7, Ca 18, Ca 4, Ca 17) trong `report/team/bang_loi.md`, đảm bảo liên kết chặt với hệ thống event (`input_validation_failed`, `refund_ledger_write`, `ticket_reopened`, `handoff_to_staff`, `audit_sample_checked`) và đề xuất thu hẹp phạm vi pilot (loại `quoc_te`), sửa khóa chống trùng/đối soát sổ cái trước khi mở pilot.
- Phối hợp cùng TV4 (`htphong23`) đối chiếu hai bộ nhãn độc lập (đạt tỉ lệ đồng thuận **20/20 = 100%**), ghi rõ quy tắc phân biệt các ca dễ nhầm theo nguyên nhân gốc và bàn giao kết quả CP3 vào mục 5 của `report/team/ho_so_launch_v0.md`.

## 4. Bằng chứng

- Nhánh làm việc: `tv3-reliability`
- File bàn giao chính: `report/team/bang_loi.md` (bảng 20 ca nhãn độc lập, tỉ lệ đồng thuận, quy tắc phân biệt và bảng khắc phục 5 ca).
- Đóng góp vào mục 5 ("Bảng lỗi và cách khắc phục") và điều kiện Go có điều kiện (sửa khóa chống trùng và đối soát sổ cái ở Ca 7, Ca 20) trong `report/team/ho_so_launch_v0.md`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Trợ lý AI (Gemini / Antigravity trong IDE).
- **Mục đích sử dụng:** Hỗ trợ trích xuất danh sách 20 ca lỗi từ file `.docx`, hệ thống hóa định nghĩa 5 nhóm lỗi theo Google PAIR và rà soát tính đo lường được (event, ngưỡng, tần suất, vai trò phụ trách) của bảng khắc phục 5 ca.
- **Cách tự kiểm tra kết quả:** Tự đọc lại từng mô tả trong 20 ca lỗi của `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, kiểm tra chéo từng nhãn theo đúng nguyên tắc "gắn theo nguyên nhân gốc, không gắn theo chỗ cần sửa" (ví dụ: phân biệt rõ Ca 6, 9 là lỗi đầu vào `Do người dùng`; Ca 8, 15 đã lộ ra nên là `Hệ thống` chứ không phải `Ngầm`; Ca 12 sai về chi phí token không ai biết suốt 3 tuần nên là `Ngầm`; Ca 13 ngoài phạm vi nên là `Giới hạn hệ thống`).

## 6. Tự đánh giá

- Hoàn thành đầy đủ, đúng hạn toàn bộ nhiệm vụ của TV3 (CP3) theo phân công nhóm.
- Tuân thủ nghiêm túc quy định liêm chính của lab: gắn nhãn 20 ca độc lập trước khi đối chiếu với TV4, giữ nguyên hai bộ nhãn gốc, không dùng từ cấm (chỉ dùng pilot/chạy thử) và chỉ định rõ một vai trò chịu trách nhiệm cho từng biện pháp khắc phục.
