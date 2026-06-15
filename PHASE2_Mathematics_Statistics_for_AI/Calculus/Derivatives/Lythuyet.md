### 1. Đạo hàm là gì? (Tốc độ thay đổi & Độ dốc)

* **Góc nhìn Đại số (Rate of change):** Đạo hàm (ký hiệu $f'(x)$ hoặc $\frac{dy}{dx}$) trả lời cho câu hỏi: *"Nếu tôi nhích biến $x$ lên một chút xíu xiu, thì hàm $y$ sẽ thay đổi bao nhiêu?"*. Nó chính là **tốc độ thay đổi**.
* **Góc nhìn Hình học (Slope):** Đạo hàm là **độ dốc của đường tiếp tuyến** chạm vào đồ thị tại một điểm.
* Nếu dốc lên (Đạo hàm $> 0$): $x$ tăng thì $y$ tăng.
* Nếu dốc xuống (Đạo hàm $< 0$): $x$ tăng thì $y$ giảm.
* Đạo hàm bằng $0$: Mặt đất bằng phẳng (Đáy thung lũng hoặc đỉnh núi).



### 2. Các quy tắc "Phá đảo" Đạo hàm

Không ai ngồi tính đạo hàm bằng giới hạn cả. Chúng ta có các công thức cốt lõi:

* **Power Rule (Quy tắc số mũ):** Nếu $f(x) = x^n \implies f'(x) = n \cdot x^{n-1}$.
*(VD: Đạo hàm của $x^2$ là $2x$. Cực kỳ hay dùng cho hàm sai số MSE của Linear Regression).*
* **Product Rule (Quy tắc tích):** $(u \cdot v)' = u'v + uv'$.
* **Chain Rule (Quy tắc chuỗi - VUA CỦA DEEP LEARNING):** Nếu hàm lồng trong hàm (giống như Lớp nơ-ron này nối tiếp Lớp nơ-ron kia): $y = f(g(x))$, thì:

$$y' = f'(g(x)) \cdot g'(x)$$



*Ý nghĩa:* Để biết thay đổi ở Lớp đầu tiên ảnh hưởng thế nào đến kết quả cuối cùng, ta cứ tính đạo hàm của từng lớp rồi **nhân chuỗi** chúng lại với nhau.

### 3. Đạo hàm của các hàm ML cốt lõi

Khi code Mạng nơ-ron, bro sẽ liên tục phải tính đạo hàm của các hàm kích hoạt (Activation functions) và hàm mất mát (Loss functions).

* **Hàm Mũ (Exp):** Cực kỳ cứng đầu. Đạo hàm của $e^x$ vẫn là chính nó: $(e^x)' = e^x$.
* **Hàm Logarit:** Đạo hàm của $\ln(x)$ là $\frac{1}{x}$. (Linh hồn của hàm sai số Cross-Entropy trong phân loại ảnh).
* **Hàm Sigmoid:** Hàm ép giá trị về khoảng $(0, 1)$ chuyên dùng cho xác suất: $\sigma(x) = \frac{1}{1 + e^{-x}}$.
* *Bí mật vi diệu:* Đạo hàm của nó tính bằng chính giá trị của nó:

$$\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))$$


* *Lợi ích:* Máy tính không cần tính lại đạo hàm từ đầu, chỉ cần lấy luôn cái kết quả đi qua ở lượt Forward pass ráp vào công thức là xong. Siêu tối ưu tốc độ!



### 4. Minima, Maxima & Saddle Points

Khi train mô hình AI, mục tiêu duy nhất của chúng ta là làm cho Hàm sai số (Loss Function) tiến về $0$. Nghĩa là ta phải dò dẫm trong không gian để tìm ra điểm thấp nhất.

* **Minima (Cực tiểu - Đáy thung lũng):** Nơi đạo hàm bằng $0$ và hai bên đều dốc lên. Đây là đích đến của mọi thuật toán AI.
* **Maxima (Cực đại - Đỉnh núi):** Nơi đạo hàm bằng $0$ nhưng hai bên dốc xuống.
* **Saddle Points (Điểm yên ngựa):** Ác mộng của Deep Learning. Đạo hàm cũng bằng $0$ (mặt phẳng), nhưng một hướng dốc lên, một hướng dốc xuống (giống cái yên ngựa). Thuật toán AI rất dễ bị "kẹt" lại đây vì tưởng nhầm là đã tới đáy.

### 5. Đạo hàm bậc 2 (Concavity & Convexity)

Đạo hàm bậc 1 ($f'$) cho biết "đang đi lên hay đi xuống". Đạo hàm bậc 2 ($f''$) cho biết "tốc độ thay đổi độ dốc đang tăng hay giảm" (Gia tốc).

* **Hàm Lồi (Convexity):** Đồ thị hình cái bát ngửa. $f''(x) > 0$. Đây là "bầu trời mơ ước" của AI vì nó đảm bảo **chỉ có 1 đáy duy nhất** (Global Minimum). Linear Regression hay SVM đều là hàm lồi.
* **Hàm Lõm (Concavity):** Đồ thị hình cái bát úp xuống. $f''(x) < 0$.

---

**🎮 Bài Tập Thực Chiến: Code Hàm Đạo Hàm Sigmoid**

Để thấm nhuần sự "tối ưu tốc độ" của thuật toán AI, bro hãy viết một script Python nhỏ:

1. Viết hàm `sigmoid(x: np.ndarray) -> np.ndarray`.
2. Viết hàm `sigmoid_derivative(x: np.ndarray) -> np.ndarray`. **Lưu ý:** Bên trong hàm này, bro bắt buộc phải tái sử dụng hàm `sigmoid(x)` vừa viết ở trên, tuân đúng theo công thức kỳ diệu $\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))$ nhé.
3. Cho mảng input `x = np.array([-1.0, 0.0, 1.0])`. Tính và in kết quả đạo hàm ra xem ở vị trí $0.0$, độ dốc lớn nhất là bao nhiêu.
