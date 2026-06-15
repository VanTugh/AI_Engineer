### 1. Sigmoid: Lão tướng mở đường

* **Công thức:** $\sigma(x) = \frac{1}{1+e^{-x}}$
* **Đạo hàm:** $\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))$
* **Vai trò:** Ép mọi số thực về khoảng $(0, 1)$. Phù hợp cho bài toán phân loại nhị phân (Ví dụ: Chó hay Mèo, Đậu hay Rớt).
* **Điểm yếu chí mạng:** Như bro đã thấy ở bài trước, đạo hàm tối đa chỉ là $0.25$. Khi qua nhiều lớp, đạo hàm bị triệt tiêu dần về 0 (**Vanishing Gradient**). Do đó, ngày nay người ta KHÔNG bao giờ dùng Sigmoid ở các lớp ẩn (Hidden layers) nữa, mà chỉ dùng ở lớp cuối cùng (Output layer).

### 2. ReLU (Rectified Linear Unit): Vị cứu tinh của Deep Learning

Đây là hàm kích hoạt được dùng nhiều nhất thế giới hiện nay (ChatGPT hay CNN đều xài nó).

* **Công thức:** $f(x) = \max(0, x)$ (Nếu âm thì bằng 0, nếu dương thì giữ nguyên).
* **Đạo hàm cực kỳ đơn giản:**
* Nếu $x > 0$: Đạo hàm $= 1$.
* Nếu $x < 0$: Đạo hàm $= 0$.


* **Sức mạnh:** Đạo hàm bằng 1 giúp cho Gradient được truyền nguyên vẹn về các lớp phía trước mà không bị hao hụt. Hơn nữa, nó tính toán bằng phép so sánh (nhanh hơn hàng vạn lần so với tính $e^{-x}$ của Sigmoid).
* **Điểm yếu:** "Dying ReLU" - nếu một nơ-ron bị âm, đạo hàm của nó vĩnh viễn bằng 0, nơ-ron đó coi như "chết lâm sàng" không bao giờ học được nữa.

### 3. Softmax: Trùm cuối Phân loại Đa lớp

Sigmoid chỉ dùng cho 2 lớp (Chó/Mèo). Nhưng nếu có 1000 lớp (1000 loại động vật) thì sao? Ta dùng Softmax.

* **Công thức:** $S_i = \frac{e^{x_i}}{\sum e^{x_j}}$
* **Vai trò:** Biến một mảng điểm số đầu ra (Logits) thành một mảng **Xác suất**, sao cho tổng xác suất của tất cả các lớp cộng lại đúng bằng $100\%$ ($1.0$).
* **Đạo hàm (Jacobian):** Hơi phức tạp vì một đầu ra ảnh hưởng đến mọi đầu vào khác. Nhưng bro không cần nhớ công thức này, vì Softmax sinh ra là để "kết hôn" với Cross-Entropy ở dưới.

### 4. Cross-Entropy Loss: Thước đo sự tự tin

Khi dự đoán xác suất, ta không dùng MSE (bình phương sai số) mà dùng Cross-Entropy.

* **Công thức lõi:** $L = - \sum y_i \log(\hat{y}_i)$ (Với $y$ là nhãn thật, $\hat{y}$ là xác suất dự đoán).
* **🪄 CÚ LỪA MA THUẬT CỦA TOÁN HỌC:** Khi bro ghép Đạo hàm của hàm Softmax nhân với Đạo hàm của hàm Cross-Entropy (Chain Rule), một đống biểu thức phức tạp sẽ tự động triệt tiêu nhau, để lại một kết quả đẹp không tưởng:

$$\text{Gradient} = \hat{y} - y$$



*(Nghĩa là: Đạo hàm chỉ đơn giản là `Dự đoán - Thực tế`. Dự đoán 0.8, thực tế là 1.0 $\rightarrow$ Gradient là -0.2. Nhanh và đẹp đến mức khó tin!)*

### 5. MSE Loss (Mean Squared Error)

Dùng cho các bài toán **Hồi quy (Regression)** như dự đoán giá nhà, dự đoán nhiệt độ (giá trị liên tục).

* **Công thức:** $L = \frac{1}{n} \sum (\hat{y} - y)^2$
* **Đạo hàm:** $\frac{\partial L}{\partial \hat{y}} = \frac{2}{n} (\hat{y} - y)$
* **Ý nghĩa:** Sai số càng lớn, đạo hàm (độ dốc) kéo về càng gắt. Khi dự đoán gần sát thực tế, đạo hàm nhỏ lại giúp mô hình đi chậm lại và hội tụ về đáy thung lũng.

---

### 🎮 Bài Tập Thực Chiến: Code ReLU siêu tốc bằng NumPy

Hãy quên cái Sigmoid chậm chạp đi, hôm nay chúng ta sẽ code "vũ khí" ReLU.

Sếp đưa cho bro một mảng dữ liệu (Vector):
`x = np.array([-2.5, 0.0, 3.1, -1.0, 5.5])`

**Nhiệm vụ của Intern:**
Viết 2 hàm cực ngắn (chỉ 1 dòng mỗi hàm), **tuyệt đối không dùng vòng lặp `for` hay `if/else**`, phải dùng sức mạnh Vectorization của NumPy:

1. `relu(x)`: Ép các số âm thành 0, số dương giữ nguyên. *(Gợi ý: Tham khảo hàm `np.maximum`).*
2. `relu_derivative(x)`: Trả về mảng chứa số $1$ (ở vị trí $x > 0$) và số $0$ (ở vị trí $x \le 0$). *(Gợi ý: Trong NumPy, biểu thức điều kiện `x > 0` sẽ trả về mảng True/False, bro chỉ cần ép kiểu nó thành số nguyên bằng `.astype(float)` hoặc `* 1.0`).*

