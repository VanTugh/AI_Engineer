
### 1. Ma trận và Phép toán cơ bản

* **Ma trận là gì?** Đơn giản là một bảng số 2 chiều (2D Array). Trong Machine Learning, số hàng (rows) thường là số lượng mẫu dữ liệu (batch size), số cột (cols) là số lượng đặc trưng (features).
* **Cộng/Trừ:** Hai ma trận phải cùng kích thước (Shape). Cộng trừ từng phần tử ở cùng vị trí với nhau.
* **Transpose (Chuyển vị - $A^T$):** Lật ngược ma trận qua đường chéo chính. Hàng biến thành cột và ngược lại. Cực kỳ hay dùng để "xoay" ma trận cho khớp kích thước trước khi nhân.

### 2. Sự khác biệt sống còn: Element-wise vs Matrix Product

Đây là cái bẫy mà 90% người mới làm AI đều đạp trúng khi code NumPy.

* **Element-wise (Nhân từng phần tử):** Ký hiệu là dấu `*` trong Python. Hai ma trận phải cùng kích thước. Nó lấy ô $(0,0)$ nhân với ô $(0,0)$. Rất hay dùng để áp dụng mặt nạ (Masking) trong Computer Vision hoặc Attention mechanism.
* **Matrix Product (Nhân ma trận chuẩn):** Toán tử `@` hoặc `np.dot()`. Luật bắt buộc: Số cột của ma trận A **phải bằng** số hàng của ma trận B.
* Kích thước: $(m \times n)$ nhân với $(n \times p)$ sẽ ra ma trận mới có kích thước $(m \times p)$.
* Phép nhân này chính là cách Mạng nơ-ron (Neural Network) truyền dữ liệu từ lớp này sang lớp khác: 
$$Y = X \cdot W + b$$





### 3. Ma trận Đơn vị (Identity) & Ma trận Nghịch đảo (Inverse)

* **Identity Matrix ($I$):** Đường chéo toàn số 1, còn lại là 0. Nó giống như số 1 trong số học. Bất kỳ ma trận nào nhân với $I$ cũng bằng chính nó ($A \cdot I = A$). Dùng `np.eye()` để tạo.
* **Inverse Matrix ($A^{-1}$):** Ma trận nghịch đảo giống như phép chia. Nếu $A$ nhân với $A^{-1}$ thì sẽ ra ma trận đơn vị $I$.
* *Lưu ý:* Không phải ma trận nào cũng có nghịch đảo. Đảo ngược một ma trận hàng triệu tham số tốn cực kỳ nhiều tài nguyên máy tính.



### 4. Định thức (Determinant) - Trực giác hình học

* **Ý nghĩa:** Định thức (Ký hiệu là $|A|$ hoặc $\det(A)$) cho biết ma trận này khi đóng vai trò là một "phép biến đổi không gian", nó sẽ làm không gian bị **phóng to hay thu nhỏ** bao nhiêu lần.
* **Cực kỳ quan trọng:** Nếu $\det(A) = 0$, nghĩa là không gian đã bị ép bẹp lép (từ 3D xuống 2D, hoặc 2D xuống 1 đường thẳng). Khi đó, lượng thông tin đã bị phá hủy và ma trận này **không thể nghịch đảo** được.

### 5. Hạng của ma trận (Rank)

* Rank đo lường **"lượng thông tin thực sự hữu ích"** trong một ma trận.
* Giả sử bro có 3 cột dữ liệu: `[Cân nặng_kg, Cân nặng_gram, Chiều cao]`. Rõ ràng cột 1 và cột 2 chứa thông tin y hệt nhau (chỉ khác tỷ lệ). Ma trận này nhìn có 3 cột, nhưng Rank (lượng thông tin độc lập) chỉ bằng 2. Trong AI, dữ liệu có Rank thấp (chứa nhiều cột thừa) sẽ làm mô hình bị nhiễu.

---

### 🎮 Bài Tập Thực Chiến: Forward Pass của Mạng Nơ-ron

Chúng ta sẽ mô phỏng một lớp (layer) của mạng Neural Network. Bro nhận được một ma trận dữ liệu đầu vào $X$ (gồm 3 bức ảnh, mỗi ảnh có 4 đặc trưng) và một ma trận Trọng số $W$.

Dữ liệu (Bro copy vào code):

```python
X = np.array([[1, 2, 3, 4], 
              [5, 6, 7, 8], 
              [9, 10, 11, 12]]) # Shape (3, 4)

W = np.array([[0.1, 0.2], 
              [0.3, 0.4], 
              [0.5, 0.6], 
              [0.7, 0.8]]) # Shape (4, 2)

bias = np.array([0.01, 0.02]) # Shape (2,)

```

**Nhiệm vụ:**

1. **Toán học:** Tính ma trận đầu ra $Y$ bằng công thức $Y = X \cdot W + bias$.
* *Gợi ý:* Dùng toán tử `@` để nhân ma trận, phép cộng `bias` NumPy sẽ tự động dùng Broadcasting (Phase 1).


2. **Thông tin:** Kiểm tra xem ma trận $W$ có chứa thông tin thừa không bằng cách in ra Rank của nó (Gợi ý: Dùng `np.linalg.matrix_rank(W)`).
3. **Tích hợp Phase 1 (Bắt buộc):**
* KHÔNG dùng `print()`, hãy setup và dùng thư viện `logging` để hiển thị kết quả.
* Tạo một **Dataclass** tên là `LayerResult` để chứa 2 thuộc tính: `output_matrix` (kiểu `np.ndarray`) và `weight_rank` (kiểu `int`).
* Viết hàm `forward_pass` có sử dụng **Type Hints**, trả về đối tượng `LayerResult` đó.
