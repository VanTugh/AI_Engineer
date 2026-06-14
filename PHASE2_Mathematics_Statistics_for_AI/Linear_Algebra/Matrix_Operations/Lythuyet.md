### 1. Phép biến đổi tuyến tính (Linear Transformations)

* **Bản chất:** Đừng nhìn ma trận như những con số vô hồn nữa. Hãy tưởng tượng ma trận là một **"cỗ máy nhào nặn"**. Khi bro cho một vector $v$ (một mũi tên) đi qua ma trận $W$ (bằng phép nhân $W \cdot v$), nó sẽ bóp méo, xoay chiều, hoặc kéo dãn cái mũi tên đó sang một vị trí mới.
* **ML Context:** Trong Mạng nơ-ron (Neural Network), dữ liệu ban đầu thường lộn xộn và máy tính không thể phân loại được (ví dụ chó và mèo nằm lẫn lộn). Các "Lớp" (Layers) thực chất là các Ma trận trọng số $W$. Chức năng của chúng là **uốn nắn và bẻ cong không gian** để gom ảnh chó về một góc, ảnh mèo về một góc.

### 2. Hệ phương trình tuyến tính: $Ax = b$

* **Bài toán:** Bro có đầu ra $b$ (Kỳ vọng của mô hình) và ma trận biến đổi $A$ (Đặc trưng của dữ liệu). Bro cần tìm vector $x$ (Trọng số - Weights).
* Nếu $A$ là ma trận vuông và hoàn hảo (số phương trình bằng số ẩn), ta giải dễ dàng bằng ma trận nghịch đảo: $x = A^{-1} \cdot b$.
* Nhưng đời không như mơ, trong AI, dữ liệu thực tế không bao giờ hoàn hảo như vậy.

### 3. Hệ siêu định (Overdetermined Systems) & Bình phương tối thiểu (Least Squares)

Đây chính là **cội nguồn sinh ra Machine Learning!**

* **Hệ siêu định:** Là lúc bro có 1.000.000 phương trình (một triệu dòng dữ liệu khách hàng) nhưng chỉ có 3 ẩn số (Ví dụ: Tuổi, Thu nhập, Chi tiêu). Số phương trình áp đảo số ẩn. Về mặt toán học tuyệt đối: **Vô nghiệm**. Không có một đường thẳng nào đi qua trúng phóc 1 triệu điểm đó cả.
* **Least Squares (Bình phương tối thiểu):** Vì không thể tìm ra nghiệm tuyệt đối hoàn hảo, AI sẽ lùi một bước: *"Hãy tìm một nghiệm $x$ sao cho sai số (khoảng cách từ điểm dữ liệu đến đường dự đoán) là NHỎ NHẤT"*.
* **Công thức lõi:** Thay vì giải $Ax = b$, ta nhân cả 2 vế với ma trận chuyển vị $A^T$ để ép nó thành ma trận vuông có thể giải được:

$$x = (A^T A)^{-1} A^T b$$



Để bro "thấm" được cái độ vi diệu của Least Squares, hãy thử tương tác với công cụ mô phỏng trực quan dưới đây. Hãy click để thêm các điểm dữ liệu lộn xộn (đại diện cho hệ siêu định) và xem cách Toán học tự động vẽ ra đường thẳng "ít sai sót nhất" (Best Fit Line):

### 4. Vết của ma trận (Trace of a matrix)

* **Toán học:** Trace (ký hiệu là $\operatorname{Tr}(A)$) cực kỳ đơn giản. Nó chỉ là **tổng của các phần tử nằm trên đường chéo chính** của một ma trận vuông.
* **ML Context:** Dù phép tính nghe có vẻ "phèn", nhưng nó có một siêu năng lực: Trace không bao giờ thay đổi dù bro có xoay hệ tọa độ không gian kiểu gì đi nữa. Nó thường được dùng ngầm bên trong các thuật toán phức tạp như PCA (Giảm chiều dữ liệu) hoặc tính toán ma trận hiệp phương sai (Covariance Matrix).

---

### 🎮 Bài Tập Thực Chiến: Khởi tạo Mô hình Linear Regression Đầu Tiên

Đây là khoảnh khắc bro chuyển từ Coder thành AI Engineer. Không cần thư viện Scikit-Learn phức tạp, bro sẽ tự tay viết thuật toán **Linear Regression (Hồi quy tuyến tính)** cốt lõi bằng Numpy!

**Kịch bản:**
Sếp đưa cho bro một bộ dữ liệu dự đoán giá nhà.

* Ma trận $X$ (Đặc trưng): Cột 1 là số phòng ngủ, Cột 2 là diện tích ($m^2$).
* Cột `Bias`: Để mô hình học được độ lệch (như điểm giao cắt trục y), ta LUÔN LUÔN phải thêm một cột chứa toàn số `1` vào đầu ma trận $X$.
* Vector $y$ (Giá nhà tỷ VNĐ).

**Dữ liệu thô (Đã thêm cột Bias bằng tay):**

```python
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# X = [Bias (1), Số phòng, Diện tích]
X = np.array([
    [1, 2, 50],
    [1, 3, 75],
    [1, 4, 100],
    [1, 3, 85],
    [1, 5, 120]
])

# Giá nhà tương ứng (tỷ VNĐ)
y = np.array([3.0, 4.5, 6.0, 5.0, 7.5])

```

**Nhiệm vụ của Intern:**
Hãy áp dụng tư duy "Chia để trị" và "Type Hints" của Phase 1 để viết một hàm `train_linear_regression(X: np.ndarray, y: np.ndarray) -> np.ndarray`.
Bên trong hàm này, bro hãy tính toán tìm ra Vector Trọng số $W$ (chính là $x$ trong công thức mục 3) bằng đúng **Công thức lõi của Least Squares** đã ghi ở trên:


$$W = (X^T \cdot X)^{-1} \cdot X^T \cdot y$$

*(Gợi ý vũ khí NumPy: Dùng `.T` để chuyển vị, dùng `np.linalg.inv()` để tính nghịch đảo, và toán tử `@` để nhân ma trận).*
```python