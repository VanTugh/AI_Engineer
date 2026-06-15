### 1. Chain Rule Đơn biến (Bóc củ hành tây)

Khi các hàm số bị lồng vào nhau, bro không thể lấy đạo hàm một phát ăn ngay được. Bro phải bóc từng lớp vỏ từ ngoài vào trong, và nhân chúng lại với nhau.

* **Toán học:** Giả sử ta có hàm $y$ lồng trong hàm $z$. Để tính đạo hàm của $z$ theo $x$:

$$\frac{dz}{dx} = \frac{dz}{dy} \cdot \frac{dy}{dx}$$


* **Ví dụ thực tế:** Bro đạp xe (x) làm xoay bánh răng (y), bánh răng làm xoay bánh xe (z).
* Bàn đạp quay 1 vòng $\implies$ Bánh răng quay 2 vòng ($\frac{dy}{dx} = 2$).
* Bánh răng quay 1 vòng $\implies$ Bánh xe quay 3 vòng ($\frac{dz}{dy} = 3$).
* $\implies$ Bàn đạp quay 1 vòng thì bánh xe quay: $2 \times 3 = 6$ vòng ($\frac{dz}{dx} = 6$).
* Đó chính là Chain Rule!



### 2. Chain Rule Đa biến (Đa đường dẫn)

Trong mạng nơ-ron, một nút (node) ở lớp trước sẽ truyền tín hiệu cho RẤT NHIỀU nút ở lớp sau.

* Nếu biến $x$ ảnh hưởng đến kết quả $L$ thông qua 2 con đường khác nhau là $y$ và $z$.
* **Quy tắc:** Đạo hàm tổng sẽ bằng **tổng của tất cả các con đường** nhân lại.

$$\frac{\partial L}{\partial x} = \left( \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial x} \right) + \left( \frac{\partial L}{\partial z} \cdot \frac{\partial z}{\partial x} \right)$$


* Đây chính là lý do vì sao mạng Neural Network càng sâu, ma trận đạo hàm cộng dồn lại càng khổng lồ.

### 3. Đồ thị Tính toán (Computational Graphs)

Máy tính cực kỳ "ngu" đại số. Nó không biết cách biến đổi phương trình rút gọn phức tạp như con người. Thay vào đó, nó chia mọi phép toán thành một **Đồ thị có hướng (Directed Graph)**. Mỗi phép tính (+, -, *, /) là một nút (Node).

Có 2 pha (Phase) chạy ngược chiều nhau trên cái đồ thị này:

**Pha 1: Forward Pass (Lan truyền xuôi - Chạy từ trái sang phải)**

* Mục tiêu: Tính ra kết quả dự đoán và **Hàm sai số (Loss)**.
* Máy tính đưa dữ liệu đầu vào ($x, y, w$), chạy qua từng phép toán, lưu lại các giá trị trung gian (local variables).

**Pha 2: Backward Pass (Lan truyền ngược - Chạy từ phải sang trái)**

* Mục tiêu: Đẩy cái "sai số" (Gradients) từ điểm cuối quay ngược về các trọng số $w$ ở đầu để cập nhật chúng.
* Nó hoạt động dựa trên 1 nguyên lý duy nhất của Chain Rule:
> **Gradient truyền về = (Gradient nhận được từ phía sau) $\times$ (Đạo hàm cục bộ của bản thân)**



---

### 🎮 Bài Tập Thực Chiến: Tự Build "Mini-PyTorch"

Để thấm nhuần thuật toán Backpropagation, bro sẽ không dùng numpy hay thư viện AI nào cả. Bro sẽ tự tay tính đạo hàm của một hàm số bằng code thuần túy qua cấu trúc Đồ thị tính toán.

**Hàm mục tiêu:** $f(x, y, z) = (x + y) \cdot z$
(Ta tách thành 2 bước cho máy tính dễ hiểu: $q = x + y$, và $f = q \cdot z$)

**Nhiệm vụ của bro:**
Hãy viết một đoạn script Python nhận vào 3 giá trị `x = -2.0`, `y = 5.0`, `z = -4.0`.

1. **Forward Pass:** Tính $q$ và tính $f$. In kết quả $f$ ra.
2. **Backward Pass:** (Bắt đầu từ $f$ lùi về $x, y, z$).
* Khởi tạo `grad_f = 1.0` (Đạo hàm của chính nó luôn bằng 1).
* Tính `grad_z` và `grad_q` dựa vào nút phép nhân $f = q \cdot z$.
* Tính `grad_x` và `grad_y` dựa vào nút phép cộng $q = x + y$ (nhớ áp dụng Chain Rule: nhân với `grad_q` được truyền từ phía sau lại).


3. In ra `grad_x`, `grad_y`, `grad_z`.
