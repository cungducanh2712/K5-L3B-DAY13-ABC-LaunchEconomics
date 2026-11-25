# Team

## Thông tin nhóm

- Tên nhóm: ABC
- Lớp: H202 - K5 L3B
- Repo nhóm: `K5-L3B-ABC-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: `https://github.com/cungducanh2712/K5-L3B-DAY13-ABC-LaunchEconomics.git`, nhánh `tv4-launch` (hoặc `main` sau khi merge)

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Cung Đức Anh | 2A202603814 | 26ai.anhcd2@vinuni.edu.vn | cungducanh2712 | Người kiểm số -> Đổi sang viết code (nửa sau) (TV2) |
|   2 | Đào Văn Hiệp | 2A202603813 | 26ai.hiepdv3@vinuni.edu.vn | daohiep2903 | Người gắn nhãn 1 (TV3) |
|   3 | Nguyễn Hồng Thắng | 2A202603829 | thangdktd@gmail.com | thangdktd | Người viết code (nửa đầu) (TV1) |
|   4 | Hoàng Thế Phong | 2A202603832 | phonghoangthe112@gmail.com | Hphong2305 | Người gắn nhãn 2 kiêm giữ hồ sơ, tích hợp (TV4) |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## CungDucAnh-2A202603814

### Phần việc phụ trách

- Nửa đầu (CP1–CP2): Người kiểm số — đối chiếu số liệu A1–A4, B1–B4, kiểm tra nhãn `simulated` và chuẩn hóa `src/lab13.py`, `report/team/bang_chi_phi.md`.
- Nửa sau (CP4–CP5): Người viết code — triển khai tính cỡ mẫu D1, tỉ lệ mở lại D3 và 3 chỉ số E1 trong `src/lab13.py`; hoàn thiện `report/team/pilot_plan.yaml` và `report/team/chi_so.md`.

### Đóng góp cụ thể

- Sửa 3 lỗi lệch rubric từ nhánh `tv1-economics` (chuyển code vào `src/lab13.py`, reset phút simulated khi giới hạn `max_lan_chay` ở B1/B3, chuẩn hóa B4 theo 9 phút và 15,3 phút/ca).
- Viết hàm `co_mau` và kiểm tra power bằng `statsmodels` (`NormalIndPower`) cho 5 câu D1, điền đủ `report/team/pilot_plan.yaml` (không còn `?`, đọc được bằng `yaml.safe_load`).
- Hoàn thiện bảng chỉ số, danh sách event có `trace_id` và bảng rủi ro kinh tế trong `report/team/chi_so.md`.

### Bằng chứng

- Nhánh `DucAnh`: commit `5f224f0`, `818eef3`, và các file `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `report/team/chi_so.md`, `report/team/2A202603814_CungDucAnh.md`.

## DaoVanHiep-2A202603813

### Phần việc phụ trách

- Phụ trách Nhiệm vụ C (CP3 — Phân tích lỗi và cách khắc phục) trên nhánh `tv3-reliability`.
- Đảm nhiệm vai trò Người gắn nhãn 1 tại Nhiệm vụ C (CP3), phân loại 20 ca lỗi theo 5 nhóm lỗi của Google PAIR.
- Lập bảng khắc phục cho 5 ca đại diện với event có `trace_id` và một vai trò phụ trách cụ thể.

### Đóng góp cụ thể

- Hoàn thành bộ nhãn 20 ca lỗi đạt tỉ lệ đồng thuận 20/20 = 100% khi đối chiếu với Người gắn nhãn 2 (TV4).
- Thiết kế giải pháp khắc phục cho 5 ca lỗi đại diện trong `report/team/bang_loi.md`.

### Bằng chứng

- Nhánh `tv3-reliability`: file `report/team/bang_loi.md`, `report/team/2A202603813_DaoVanHiep.md`.

## Nguyễn Hồng Thắng-2A202603829

### Phần việc phụ trách

- Nửa đầu (CP1–CP2): Người viết code (TV1) trên nhánh `tv1-economics`.
- Xây dựng mô hình chi phí A1–A4 và phân tích độ nhạy B1–B4.

### Đóng góp cụ thể

- Viết các hàm kinh tế chạy lại và mô hình chi phí từ trace trong `src/economics.py`.
- Điền các bảng số liệu chi phí và độ nhạy trong `report/team/bang_chi_phi.md`.

### Bằng chứng

- Nhánh `tv1-economics`: commit `73b6108`, file `src/economics.py`, `report/team/bang_chi_phi.md`.

## Hoàng Thế Phong-2A202603832

### Phần việc phụ trách

- Người gắn nhãn 2 kiêm giữ hồ sơ, tích hợp (TV4 — CP5) trên nhánh `tv4-launch`.
- Phụ trách chính Nhiệm vụ E1, E2, E3 và gắn nhãn độc lập Nhiệm vụ C.

### Đóng góp cụ thể

- Viết script và kiểm tra 3 chỉ số từ CSV, đặc tả 10 event có `trace_id` và 3 dòng rủi ro kinh tế trong `report/team/chi_so.md`.
- Gắn nhãn độc lập 20 ca lỗi ở `report/team/bang_loi.md` đạt đồng thuận 100%.
- Dựng và hoàn thiện hồ sơ launch v0 một trang [report/team/ho_so_launch_v0.md](report/team/ho_so_launch_v0.md) với đề xuất Go có điều kiện.
- Tích hợp toàn bộ nhánh làm việc của cả nhóm, rà soát sạch 100% từ cấm và dấu hỏi trong YAML.

### Bằng chứng

- Nhánh `tv4-launch`: commit `223736b`, `852b0e4`, `f009196`, `6986b06`, các file `src/metrics.py`, `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md`.
