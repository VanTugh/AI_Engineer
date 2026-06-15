### 1. Partial Derivatives (Đạo hàm riêng)

Ở trên, ta chỉ xét hàm 1 biến $x$. Nhưng Mạng nơ-ron có hàng triệu biến (Weights $w_1, w_2, w_3...$).
Khi ta đứng trên một ngọn núi 3D, ta không chỉ có tiến/lùi, mà còn có sang trái/sang phải.

* **Đạo hàm riêng theo x ($\frac{\partial f}{\partial x}$):** Giữ nguyên trục y, bước 1 bước theo trục x xem độ dốc là bao nhiêu.
* **Đạo hàm riêng theo y ($\frac{\partial f}{\partial y}$):** Giữ nguyên trục x, bước 1 bước theo trục y xem độ dốc là bao nhiêu.

### 2. Gradient (Vector Gradient - $\nabla f$)

Gradient là một Vector gom tất cả các Đạo hàm riêng lại với nhau. Ví dụ: $\nabla f = [\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}]$.

* **TÍNH CHẤT MA THUẬT:** Vector Gradient LUÔN LUÔN chỉ về hướng dốc nhất để **đi lên đỉnh núi** (Steepest Ascent).
* Nhưng trong AI, hàm Loss Function của chúng ta đo lường "Sai số". Ta muốn sai số càng nhỏ càng tốt, nghĩa là ta muốn **đi xuống đáy thung lũng**. Vậy phải làm sao? Rất đơn giản: Ta đi ngược chiều Gradient (nhân thêm dấu âm $-\nabla f$).

### 3. Gradient Descent (Thuật toán Giảm độ dốc)

Đây là thuật toán trị giá hàng tỷ đô la đang điều khiển ChatGPT, Tesla Autopilot hay Tiktok thuật toán. Thuật toán hoạt động theo các bước:

1. **Đoán bừa (Random Initialization):** Khởi tạo một điểm ngẫu nhiên trên sườn núi.
2. **Đo độ dốc (Calculate Gradient):** Tính $\nabla f$ tại điểm đó để biết hướng nào dốc nhất.
3. **Bước đi (Update Rule):** Xoay người đi ngược hướng Gradient một bước nhỏ.
* Công thức vĩ đại: 
$$W_{new} = W_{old} - \alpha \cdot \nabla f(W_{old})$$


* $\alpha$ (Alpha) ở đây là **Learning Rate (Tốc độ học)**. Nó quy định bước chân của bro dài hay ngắn. Bước quá ngắn thì đi nghìn năm mới tới đáy. Bước quá dài thì sẽ bị trượt chân nhảy vọt qua bên kia bờ vực.



---

### 🎮 Bài Tập Thực Chiến: Tự code Thuật toán vĩ đại nhất

Sếp giao cho bro một hàm số đơn giản (hình cái bát): $y = f(x) = x^2$.
Đáy của cái bát này hiển nhiên nằm ở $x = 0$. Nhưng bro phải dùng code để máy tính "nhắm mắt dò đường" tự tìm ra cái đáy đó!

* **Toán học:** Đạo hàm của $x^2$ là $2x$. Vậy Gradient là $\nabla f(x) = 2x$.
* **Điểm xuất phát:** Thả máy tính rơi xuống sườn núi tại vị trí $x = 5.0$.
* **Learning Rate ($\alpha$):** Đặt là `0.1`.

**Nhiệm vụ của Intern:**

1. Viết một vòng lặp `for` chạy 20 lần (đại diện cho 20 bước đi).
2. Trong mỗi bước, cập nhật lại giá trị của $x$ theo đúng công thức vĩ đại ở trên: `x = x - learning_rate * (2 * x)`.
3. In ra vị trí của $x$ ở từng bước để xem cách máy tính "lăn" dần về vị trí đáy $0.0$ cực kỳ vi diệu. (Bro có thể dùng thư viện `logging`).

