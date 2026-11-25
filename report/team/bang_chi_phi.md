# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/economics.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,2000 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,2500 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,2500 |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated |
| Số việc thành công | 978 | `ket_qua` | đo từ trace |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 275 | | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? Gấp **16,28 lần** (4.472 đ so với 275 đ).
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại** (`simulated`) chiếm tỉ trọng lớn nhất: **51,8%** (2.264.000 / 4.373.585 đ), tiếp theo là **Xem lại** (`simulated`) 40,7%.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 | -9.304 |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 | -3.779 |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 | +10.515 |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 | -1.785 |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`** không đáng để trợ lý xử lý vì chi phí mỗi việc thành công là **22.515 đ** (`simulated`), cao hơn 10.515 đ so với 12.000 đ; chạy lại tới 3 lần vẫn chỉ đạt 27,3% thành công nên không giúp được.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 | 4.599 | -7.401 |
| Một nửa khối lượng | 16.875 | 2.370 | 5.784 | -6.216 |

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Không đổi kết luận ở cả hai mức: ngay cả khi giảm một nửa khối lượng (22.500 yêu cầu/tháng), tổng chi phí mỗi việc vẫn là **5.784 đ** (`simulated`), thấp hơn 6.216 đ so với mức 12.000 đ.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 | -2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 | -20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 | -25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.488 | +0,4% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.858 | +8,6% |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ** (`simulated`), tăng **+46,3%** so với mức gốc 4.472 đ.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: **1. Số ca làm lại (+51,8% / -25,9%) · 2. Tỉ lệ xem lại (+40,7% / -20,3%) · 3. Lương nhân viên (+23,1%)**.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 4.279.781 | 319 | 8.107.781 | 4.858 |
| 2 lần | 4.335.220 | 234 | 7.143.220 | 4.488 |
| 3 lần | 4.373.585 | 222 | 7.037.585 | 4.472 |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **3 lần** là rẻ nhất cho công ty (**7.037.585 đ** cả hệ thống, `simulated`) và trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất (**4.472 đ**).

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **12.962 đ** (`simulated`, trung bình 5,03 phút xem lại/ca), cao hơn **+962 đ** so với 12.000 đ.
- Kết quả này nói gì về thứ pilot cần học được? Nếu nhân viên phải xem lại 100% thì trợ lý đắt hơn tự làm; pilot cần học **tỉ lệ xem lại tối thiểu đủ an toàn** (chỉ xem lại chọn lọc) và giảm tỉ lệ làm lại.
