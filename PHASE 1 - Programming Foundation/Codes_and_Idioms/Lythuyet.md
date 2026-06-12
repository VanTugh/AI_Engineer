### 1. Comprehensions (List, Dict, Set) - Vua rút gọn code

Thay vì tạo list rỗng rồi dùng `for` và `append`, bro ép tất cả vào 1 dòng. Tốc độ thực thi nhanh hơn vòng lặp thường rất nhiều.

* **List Comprehension:** Lọc các bounding box có độ tự tin cao trong Computer Vision.
```python
scores = [0.9, 0.2, 0.85, 0.4]
# Chỉ giữ lại score > 0.5
high_scores = [s for s in scores if s > 0.5] 

```


* **Dict Comprehension:** Đổi chỗ Key-Value cực nhanh.
```python
label_to_id = {"cat": 0, "dog": 1}
id_to_label = {v: k for k, v in label_to_id.items()} # {0: 'cat', 1: 'dog'}

```



### 2. Generator Expressions - "Phao cứu sinh" chống tràn RAM

Cú pháp y hệt List Comprehension nhưng dùng **ngoặc tròn `()**`.

* **Khác biệt cốt lõi:** List Comprehension tạo ra toàn bộ dữ liệu tống thẳng vào RAM. Generator chỉ tạo ra **từng phần tử một** khi được gọi (lazy evaluation).
* **Ứng dụng Big Data:** Nếu bro cần đọc 1 file log/text nặng 10GB, dùng Generator sẽ giúp RAM của bro chỉ tiêu tốn vài MB, mô hình không bao giờ bị Crash (OOM - Out of Memory).

### 3. Unpacking với `*rest` (Tuyệt kỹ Deep Learning)

Khi làm việc với các Tensor (ma trận nhiều chiều), bro thường xuyên phải tách kích thước (shape) của chúng ra.

```python
tensor_shape = (32, 3, 224, 224) # (batch_size, channels, height, width)

# Unpacking lấy batch_size, gom toàn bộ phần còn lại vào image_dims
batch, *image_dims = tensor_shape 
# Kết quả: batch = 32, image_dims = [3, 224, 224]

```

### 4. `any()`, `all()`, và `sorted()` với `key`

* **`any()` / `all()`:** Kiểm tra điều kiện trên toàn bộ tập dữ liệu cực nhanh.
* *Vd:* `if any(loss > 100 for loss in batch_losses): print("Cảnh báo: Gradient bùng nổ!")`


* **`sorted(iterable, key=...)`:** Sắp xếp dữ liệu phức tạp. Rất hay dùng kết hợp với hàm ẩn danh `lambda`.
* *Vd:* Sắp xếp danh sách dự đoán theo độ tự tin giảm dần: `sorted(predictions, key=lambda x: x['confidence'], reverse=True)`



### 5. `collections` module - Kho báu bị bỏ quên

Thư viện chuẩn của Python có 3 cấu trúc dữ liệu cực mạnh cho AI:

* **`Counter`:** Máy đếm siêu tốc. Ném một list từ vựng vào, nó tự động đếm tần suất xuất hiện của từng từ (rất cần khi build Vocabulary trong NLP).
* **`defaultdict`:** Giống Dict thường, nhưng nếu gọi một Key chưa tồn tại, nó không báo lỗi `KeyError` mà tự khởi tạo giá trị mặc định (như list rỗng hay số 0). Rất tiện khi gom nhóm dữ liệu.
* **`deque`:** Hàng đợi 2 đầu. Đặc điểm bá đạo là giới hạn được kích thước (`maxlen`). Khi thêm phần tử mới, phần tử cũ nhất sẽ tự bị đẩy ra.
* *Ứng dụng:* Tính Moving Average của Loss function trong $N$ batch gần nhất.



---

### 🎮 Bài Tập Thực Chiến: Tổng duyệt Stage 1

Đây là 2 bài toán ghép kỹ năng để bro chốt sổ phần Python Foundation này nhé:

**Bài 1: Sát thủ Comprehension & Unpacking**
Bro nhận được shape của một batch video từ mô hình 3D CNN:
`video_shape = (16, 3, 30, 256, 256)` tương ứng với `(batch_size, channels, frames, height, width)`.

1. Hãy dùng kỹ thuật Unpacking để gán giá trị 16 cho biến `batch`, gán 3 cho biến `channels`, và gom cụm `(30, 256, 256)` vào một list có tên là `spatial_dims`.
2. Dùng List Comprehension để nhân đôi kích thước của mọi phần tử trong `spatial_dims`. (Kỳ vọng kết quả mới: `[60, 512, 512]`).

**Bài 2: Thống kê Data với `collections**`
Bro có một list các nhãn (labels) do mô hình dự đoán ra:
`preds = ["cat", "dog", "cat", "bird", "cat", "dog"]`

1. Hãy import công cụ phù hợp từ thư viện `collections`.
2. Trích xuất ra top 1 con vật xuất hiện nhiều nhất và số lần xuất hiện của nó (Gợi ý: Tìm hiểu method `most_common()` của công cụ đó).
