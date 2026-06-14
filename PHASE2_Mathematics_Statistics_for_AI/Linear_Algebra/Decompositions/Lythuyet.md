### 1. Eigenvalues & Eigenvectors (Trị riêng & Vector riêng) - Những kẻ ngoan cố

* **Trực giác hình học:** Khi bro dùng một ma trận để kéo dãn hay bóp méo không gian (như việc kéo căng một tấm vải cao su), hầu hết các vector (mũi tên) sẽ bị **lệch hướng**. Tuy nhiên, có một vài mũi tên cực kỳ "ngoan cố", chúng **chỉ bị dài ra hoặc ngắn đi chứ tuyệt đối không đổi hướng**.
* Các mũi tên ngoan cố đó gọi là **Eigenvectors**.
* Hệ số dãn ra/co lại của chúng gọi là **Eigenvalues** ($\lambda$).


* **Công thức lõi:**

Ax = \lambda x



*(Nhân ma trận A với vector x cũng chỉ tương đương với việc lấy một con số $\lambda$ nhân với $x$).*

### 2. Tại sao Eigenvalues lại quyết định sự sống còn trong PCA?

* **PCA (Principal Component Analysis - Phân tích thành phần chính):** Là kỹ thuật gom nhóm dữ liệu. Giả sử bro có 1000 đặc trưng của một căn nhà, bro không thể vẽ đồ thị 1000 chiều được. Bro cần ép nó xuống 2D hoặc 3D.
* **Góc nhìn tối ưu:** Giống như việc chụp ảnh một cái ấm trà. Chụp từ trên xuống chỉ thấy hình tròn (mất thông tin). Chụp ngang mới thấy vòi và quai ấm.
* **Mối liên hệ:** Trong PCA, ta tìm Eigenvectors của ma trận Hiệp phương sai (Covariance Matrix).
* **Eigenvectors** chính là những "góc chụp" (trục tọa độ mới).
* **Eigenvalues** chính là lượng thông tin (phương sai) mà góc chụp đó bắt được. Eigenvalue càng lớn, thông tin càng nhiều $\rightarrow$ Ta giữ lại. Eigenvalue quá nhỏ $\rightarrow$ Ta vứt đi (Giảm chiều).



Để bro hình dung rõ hơn quá trình ép dữ liệu từ 2D xuống 1D (Dimensionality Reduction) bằng PCA, hãy thử nghịch trực tiếp với hệ thống này:

### 3. SVD (Singular Value Decomposition) - Thuyết vạn vật của Ma trận

Eigen-decomposition ở trên rất xịn, nhưng nó có một điểm yếu chí mạng: Nó chỉ chạy được trên **Ma trận vuông** (số hàng = số cột). Mà đời thì toàn ma trận chữ nhật (1 triệu khách hàng x 50 tính năng). SVD ra đời để cứu thế giới.

* SVD chứng minh được rằng: **MỌI ma trận** dù méo mó cỡ nào cũng có thể tách thành 3 ma trận cơ bản:

$$A = U \cdot \Sigma \cdot V^T$$


* **Ý nghĩa hình học siêu việt:** Mọi phép biến đổi dữ liệu lộn xộn đều có thể phân rã thành đúng 3 bước:
1. $V^T$: **Xoay** hệ tọa độ.
2. $\Sigma$: **Kéo dãn/Ép nén** dọc theo các trục (chứa các Singular Values).
3. $U$: **Xoay** hệ tọa độ thêm lần nữa.



### 4. SVD và Dimensionality Reduction (Kỹ năng nén thông tin)

Ma trận $\Sigma$ chứa các Singular Values ($s_1, s_2, ...$). Một điều kỳ diệu là tự nhiên luôn sắp xếp chúng từ lớn nhất đến nhỏ nhất.

* Ví dụ: Bức ảnh con mèo có độ phân giải 1000x1000 pixels (tức là 1 triệu con số). Sau khi phân rã SVD, nó tạo ra 1000 Singular Values.
* Nhưng chỉ có khoảng 50 giá trị đầu tiên là cực lớn (chứa thông tin về mắt, mũi, râu mèo), 950 giá trị còn lại cực bé (chứa thông tin về hạt nhiễu, background lờ mờ).
* **Tuyệt chiêu (Truncated SVD):** Ta chỉ giữ lại $k = 50$ giá trị lớn nhất, xóa sạch phần còn lại. Khi nhân ngược 3 ma trận lại ($U_k \cdot \Sigma_k \cdot V^T_k$), ta thu lại được ảnh con mèo giống 99% bản gốc, nhưng dung lượng file giảm đi 20 lần!

---

### 🎮 Bài Tập Thực Chiến: Kỹ Sư Nén Dữ Liệu SVD

Sếp vừa gửi cho bro một ma trận dữ liệu giả lập có kích thước $(100, 50)$ (100 dòng, 50 cột). Sếp yêu cầu bro nén nó xuống chỉ còn 5 cột (chiều) nhưng vẫn phải giữ lại được hình dáng gốc của dữ liệu.

*(Gợi ý vũ khí của Phase 1: Nhớ dùng `logging` và Type Hints nhé!)*

```python
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Giả lập ma trận dữ liệu (100 dòng, 50 cột)
# Để mô phỏng dữ liệu có tính quy luật, ta tạo một ma trận Rank thấp (Rank = 5) rồi cộng thêm chút nhiễu
np.random.seed(42)
hidden_factors = np.random.randn(100, 5)
weights = np.random.randn(5, 50)
noise = np.random.randn(100, 50) * 0.1

X_original = hidden_factors @ weights + noise 

```

**Nhiệm vụ của bro:**

1. Hãy viết hàm `compress_data_svd(X: np.ndarray, k: int) -> np.ndarray`.
2. Trong hàm này, dùng `U, S, Vt = np.linalg.svd(X, full_matrices=False)` để phân rã SVD. *(Lưu ý: `S` trả về chỉ là mảng 1D, bro muốn nhân ma trận thì phải biến nó thành ma trận đường chéo bằng `np.diag(S)`).*
3. Cắt (Slice) lấy đúng $k$ thành phần đầu tiên của $U$, $S$, và $Vt$.
4. Nhân 3 ma trận bị cắt đó lại với nhau để tạo ra ma trận phục hồi `X_reconstructed`.
5. Ở phần `__main__`, gọi hàm với $k=5$. Sau đó dùng `np.linalg.norm(X_original - X_reconstructed)` để tính xem sai số (tổng thất thoát thông tin) là bao nhiêu, và in ra bằng `logging`.

