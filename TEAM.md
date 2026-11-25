# Team

## Thông tin nhóm

- Tên nhóm:
- Lớp: L3A hoặc L3B
- Repo nhóm: `K5-L3A-DAY13-TenNhom-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Cung Đức Anh | 2A202603814 | 26ai.anhcd2@vinuni.edu.vn | cungducanh2712 | Người kiểm số -> Đổi sang viết code (nửa sau) |
|   2 |        |      |       |        |         |
|   3 |        |      |       |        |         |
|   4 |        |      |       |        |         |

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
