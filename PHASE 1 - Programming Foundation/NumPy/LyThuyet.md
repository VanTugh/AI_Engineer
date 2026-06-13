### 1. Khởi tạo & Thông tin mảng (Attributes)

* `np.array()`: Ép list thành mảng NumPy.
* `np.zeros()`, `np.ones()`: Tạo ma trận toàn 0 hoặc 1 (hay dùng để khởi tạo bias).
* `np.eye()`: Ma trận đơn vị (đường chéo bằng 1).
* **Bộ 3 sống còn:** * `shape`: Hình dáng ma trận (VD: ảnh RGB là `(3, 224, 224)`).
* `ndim`: Số chiều.
* `dtype`: Kiểu dữ liệu (Train Deep Learning thường ép về `float32` để tiết kiệm một nửa RAM GPU so với `float64`).

### 2. Nhào nặn hình khối (Reshape & Flatten)

* `reshape()`: Bẻ cong ma trận miễn là tổng số phần tử không đổi. VD: Đưa mảng 1D `(784,)` về ảnh 2D `(28, 28)`.
* **`flatten()` vs `ravel()`:** Đều dùng để duỗi thẳng ma trận thành 1D. Nhớ kỹ: `flatten()` xài tốn RAM hơn vì nó tạo ra một **bản sao mới (Deep Copy)**, còn `ravel()` tạo ra một **góc nhìn (View)** trỏ về bộ nhớ gốc nên cực nhanh.
* `np.stack()`, `np.hstack()` (ghép ngang), `np.vstack()` (ghép dọc): Dùng để gom các ảnh lẻ tẻ thành một Batch lớn tống vào model.

### 3. Phép thuật AI: Broadcasting & `np.where`

* **Broadcasting:** Luật tự động "nhân bản" của NumPy. Bro có thể lấy ma trận `(3, 3)` cộng trực tiếp với một vector `(3,)`. NumPy tự động copy cái vector đó thành 3 dòng để cộng mà không cần bro viết vòng lặp.
* **`np.where(condition, x, y)`:** Hàm rẽ nhánh siêu tốc.
* *Ứng dụng ML:* Hàm kích hoạt **ReLU** huyền thoại chỉ đơn giản là `np.where(arr > 0, arr, 0)` (Nếu dương thì giữ nguyên, âm thì cho thành 0).



### 4. Đại số tuyến tính (Linear Algebra)

* **Nhân ma trận:** Bắt buộc dùng `np.dot(A, B)` hoặc toán tử `@` (VD: `A @ B`).
* *Tuyệt đối tránh:* Dùng dấu `*` vì nó chỉ là nhân từng phần tử cùng vị trí (Element-wise).


* `np.linalg.inv()`: Nghịch đảo ma trận.
* `np.linalg.eig()`: Tìm trị riêng, vector riêng (Dùng trong thuật toán giảm chiều dữ liệu PCA).

### 5. Khử chiều dữ liệu (Aggregations & Axis)

Khi tính tổng `sum()`, trung bình `mean()`, hay lớn nhất `max()`, việc chọn đúng **`axis`** là cốt lõi.

* `axis=0`: Trượt dọc theo cột (xóa xổ số hàng).
* `axis=1`: Trượt ngang theo hàng (xóa xổ số cột).

### 6. Khởi tạo ngẫu nhiên (`np.random`)

Module sinh số ngẫu nhiên cực mạnh. Các hàm `np.random.rand()` (phân phối đều), `randn()` (phân phối chuẩn) được dùng để khởi tạo trọng số ngẫu nhiên cho mạng nơ-ron trước khi train.

---

### 🎮 Bài Tập Thực Chiến: Xử lý Tensor giả lập

Hãy import numpy `import numpy as np` và giải quyết 2 bài toán xử lý Data Pipeline dưới đây:

**Bài 1: Xây dựng hàm kích hoạt ReLU & Reshape**

1. Khởi tạo một mảng 1D gồm 9 phần tử ngẫu nhiên (có cả âm và dương): `arr = np.array([-2, 1, 5, -5, 8, -1, 3, -4, 0])`
2. Dùng `reshape` biến nó thành ma trận ảnh 2D kích thước `(3, 3)`.
3. Dùng `np.where` để áp dụng luật ReLU: Thay thế toàn bộ số âm trong ma trận thành `0`, số dương giữ nguyên. In ra kết quả.

**Bài 2: Tính sai số (Loss) với Axis**
Trong 1 batch có 3 tấm ảnh, mô hình dự đoán ra 3 vector xác suất (mỗi vector có 4 class).

* `y_pred = np.array([[0.1, 0.2, 0.6, 0.1], [0.8, 0.1, 0.05, 0.05], [0.2, 0.5, 0.2, 0.1]])`
* `y_true = np.array([[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]])`

1. Tính ma trận sai số: `error = y_pred - y_true`.
2. Bình phương ma trận sai số vừa tính (dùng toán tử ` 2`).
3. Dùng `.mean(axis=...)` để tính sai số trung bình (MSE) cho **TỪNG MẪU** trong batch (Kỳ vọng kết quả là một mảng 1D có 3 phần tử, mỗi phần tử đại diện cho loss của 1 bức ảnh). In ra kết quả này.