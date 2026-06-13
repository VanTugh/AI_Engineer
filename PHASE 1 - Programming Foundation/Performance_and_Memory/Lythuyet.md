
### 1. Generators và `yield` (Phao cứu sinh của RAM)

Trong Python bình thường, khi dùng `return`, hàm sẽ tính toán toàn bộ kết quả, nén cục vào RAM rồi mới trả về. Nếu data là 10 triệu dòng văn bản, máy tính sẽ báo lỗi OOM (Out of Memory) ngay lập tức.

* **`yield`**: Thay vì trả về một cục, `yield` trả về **từng phần tử một**, sau đó hàm sẽ "tạm dừng" (pause) trạng thái. Gọi lần tiếp theo nó mới tính tiếp.
* **Ứng dụng AI:** * **Streaming LLM:** Chữ tự động gõ ra trên màn hình giống ChatGPT chính là nhờ cơ chế sinh từng token bằng `yield`.
* **Data Loader:** Load từng batch dữ liệu vài trăm MB đưa vào GPU train, train xong vứt đi load batch mới, không bao giờ đầy RAM.



### 2. Module `itertools` (Lắp motor cho vòng lặp)

Thư viện chuẩn của Python chứa các vòng lặp viết bằng ngôn ngữ C cực nhanh.

* `itertools.cycle(data)`: Lặp vô tận một mảng (cực hữu ích khi viết training loop chạy liên tục qua nhiều epochs).
* `itertools.islice(generator, n)`: Cắt lấy `n` phần tử từ một luồng generator khổng lồ mà không cần load hết vào bộ nhớ.

### 3. Profiling (Đo lường hiệu năng)

Đừng bao giờ đoán xem code chậm ở đâu, hãy đo lường chính xác.

* **`timeit`**: Module dùng để đo tốc độ thực thi của một đoạn code nhỏ (chạy 10.000 lần xem tốn bao nhiêu mili-giây).
* **`cProfile`**: Khi bro có một pipeline dài dằng dặc, chạy `cProfile.run('main()')` nó sẽ quét và in ra một bảng báo cáo: Hàm nào được gọi bao nhiêu lần, ngốn bao nhiêu % thời gian CPU. Đây là vũ khí săn "nút thắt cổ chai" (bottleneck).

### 4. Shallow vs Deep Copy (Cạm bẫy nhân bản)

Trong quá trình thử nghiệm (experiment) nhiều cấu hình (config) khác nhau cho model, bro thường phải copy một dictionary config gốc ra để sửa.

* **Toán tử gán (`=`)**: Không phải copy, hai biến cùng trỏ vào 1 ô nhớ. Sửa A là B chết.
* **Shallow Copy (`copy.copy()` hoặc `list.copy()`)**: Copy được lớp bên ngoài, nhưng nếu bên trong chứa List lồng List (Nested), các List bên trong vẫn bị dính chung ô nhớ!
* **Deep Copy (`copy.deepcopy()`)**: An toàn tuyệt đối. Đào sâu xuống tận cùng và tạo ra các ô nhớ hoàn toàn mới cho mọi cấp độ.

### 5. Vectorization vs Python loops (Tư duy của Deep Learning)

Trong AI, **KHÔNG BAO GIỜ** dùng vòng lặp `for` để nhân hai ma trận hay tính toán toán học trên các mảng lớn. Python loop rất chậm.

* **Vectorization**: Kỹ thuật ép toàn bộ mảng dữ liệu vào các phép toán của C/C++ dưới nền (thông qua NumPy hoặc PyTorch). Thay vì lặp `for i in range(len(A)): C[i] = A[i] + B[i]`, bro chỉ việc viết `C = A + B`. Tốc độ có thể nhanh hơn gấp 100 lần!

---

### 🎮 Bài Tập Thực Chiến: Giải cứu RAM & Bẫy Copy

Để nắm trọn tinh hoa của 1.7, bro hãy xử lý 2 vấn đề sau:

**Bài 1: Streamer với `yield**`
Giả sử bro có một luồng dữ liệu thô (tượng trưng bằng một `range(1, 100)`). Bro không được phép dùng `return` cả mảng.

* Hãy viết một hàm `batch_generator(data, batch_size)` sử dụng vòng lặp và `yield` để mỗi lần gọi, nó sẽ "nhả" ra một list con có kích thước bằng `batch_size`.
* *(Gợi ý: Dùng vòng lặp bước nhảy step `for i in range(0, len(data), batch_size):`)*

**Bài 2: Gỡ bom Shallow Copy**
Bro có một file cấu hình mô hình rất phức tạp (Nested Dictionary):

```python
import copy

base_config = {
    "model_name": "CNN",
    "layers": [64, 128, 256],  # List nằm bên trong Dict
    "learning_rate": 0.001
}

# Bro muốn tạo config_2 để thử nghiệm, giữ nguyên mọi thứ nhưng đổi layer cuối
config_2 = base_config.copy() # Đang dùng Shallow Copy
config_2["layers"][2] = 512

```

* Hỏi: Nếu in `base_config["layers"]` ra lúc này, mảng `layers` của cấu hình gốc có bị thay đổi thành 512 không?
* Nếu bị đổi, bro phải dùng lệnh gì của module `copy` để sửa lỗi này?
