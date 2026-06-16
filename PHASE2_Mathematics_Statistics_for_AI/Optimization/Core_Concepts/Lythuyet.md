### 1. Objective Function vs Loss Function (Kim chỉ nam của AI)

Nhiều người mới học rất hay lẫn lộn hai khái niệm này, nhưng phân biệt chúng rất dễ:

* **Objective Function (Hàm mục tiêu):** Là mục tiêu tối thượng mà mô hình cần đạt được. Nó có thể là đi tìm điểm cao nhất (Tối đa hóa lợi nhuận) hoặc điểm thấp nhất (Tối thiểu hóa rủi ro).
* **Loss/Cost Function (Hàm mất mát):** Là một loại Hàm mục tiêu đặc biệt, chuyên dùng để đo lường **Sai số**. Trong Machine Learning, chúng ta luôn muốn sai số càng nhỏ càng tốt, nên bài toán Tối ưu hóa trong AI mặc định là bài toán **Minimization (Tìm cực tiểu)**.

### 2. Convex vs Non-convex Functions (Thiên đường và Địa ngục)

Địa hình Toán học chia làm 2 loại cơ bản, và đây là thứ quyết định AI của bro học nhanh hay chậm.

* **Convex Function (Hàm lồi - Thiên đường):** * *Hình dáng:* Giống như một cái bát trơn tuột.
* *Đặc điểm:* Chỉ có duy nhất một điểm thấp nhất. Bất kể bro thả viên bi (khởi tạo trọng số ngẫu nhiên) ở đâu trên miệng bát, nó cũng tự động lăn về đúng cái đáy đó.
* *Thuật toán áp dụng:* Linear Regression, Support Vector Machine (SVM). Đây là những bài toán giải phát ăn ngay, chắc chắn ra nghiệm tối ưu.


* **Non-convex Function (Hàm không lồi - Địa ngục):**
* *Hình dáng:* Giống như dãy núi Alps với hàng vạn thung lũng, đỉnh đèo khúc khuỷu.
* *Đặc điểm:* Cực kỳ gập ghềnh. Viên bi lăn xuống rất dễ bị kẹt lại ở một thung lũng nhỏ nằm lơ lửng trên sườn núi.
* *Thuật toán áp dụng:* **Deep Learning (Mạng nơ-ron).** Hàm Loss của Mạng nơ-ron là một hàm Non-convex siêu phức tạp trong không gian hàng tỷ chiều!



### 3. Local Minima, Global Minima & Saddle Points (Những cái bẫy chết người)

Khi thả AI chạy trong thế giới Non-convex của Mạng nơ-ron, nó sẽ phải đối mặt với 3 vị trí địa lý sau:

* **Global Minima (Cực tiểu toàn cục):** Điểm sâu nhất của toàn bộ dãy núi. Nơi Loss thấp nhất, mô hình hoàn hảo nhất. Đích đến trong mơ!
* **Local Minima (Cực tiểu cục bộ):** Một cái thung lũng cạn. Máy tính dò đạo hàm (Gradient) thấy độ dốc bằng `0.0`, tưởng là tới đáy rồi nên cắm cờ dừng lại (Early Stopping). Kết quả là AI bị "học ngu" do kẹt ở đáy giả.
* **Saddle Points (Điểm yên ngựa):** Ác mộng tồi tệ nhất của không gian đa chiều!
* Hãy tưởng tượng cái yên ngựa: Nhìn từ đằng trước ra đằng sau thì nó là cái đáy (lõm xuống), nhưng nhìn từ bên trái sang bên phải thì nó lại là cái đỉnh (lồi lên).
* Ở chính giữa yên ngựa, đạo hàm bằng `0.0`. Thuật toán Gradient Descent cơ bản lao vào đây sẽ bị bối rối không biết đi hướng nào và đứng im mãi mãi. Khổ nỗi, trong không gian hàng triệu chiều của Deep Learning, tỷ lệ gặp Saddle points cao gấp hàng vạn lần so với gặp Local minima!



### 4. Constrained vs Unconstrained Optimization (Ràng buộc và Tự do)

Làm sao để giới hạn vùng tìm kiếm của AI?

* **Unconstrained Optimization (Tối ưu không ràng buộc):** Bro thả thuật toán Gradient Descent chạy tự do trong không gian. Nó muốn bóp méo Trọng số (Weights) lên tới 1 tỷ hay âm 1 tỷ cũng được, miễn là Loss giảm.
* **Constrained Optimization (Tối ưu có ràng buộc):** AI vẫn phải tìm đáy, nhưng bị nhốt trong một cái "vòng kim cô" (Điều kiện).
* *Ví dụ 1:* Hàm Softmax ép AI tìm xác suất sao cho tổng của chúng bắt buộc phải bằng `1.0`.
* *Ví dụ 2 (L1/L2 Regularization):* Sếp yêu cầu AI tối ưu hóa sai số, nhưng thêm điều kiện: Tổng bình phương các Trọng số không được vượt quá một hằng số $C$. Nếu AI đẩy trọng số lên quá cao (học vẹt - Overfitting), nó sẽ bị "phạt" và văng ra ngoài ranh giới.



---

**🎮 Code Thí Nghiệm: Khám Phá Địa Hình Non-Convex**

Để bro thấy rõ thuật toán bị "kẹt" như thế nào, hãy chạy thử đoạn code mô phỏng hàm Non-convex dưới đây. Tôi dùng một hàm đa thức có nhiều nếp gấp: $f(x) = x^4 - 4x^2 + x$.

```python
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

def f(x):
    """Hàm Non-convex hình chữ W lệch"""
    return x**4 - 4*x**2 + x

def gradient(x):
    """Đạo hàm: 4x^3 - 8x + 1"""
    return 4*x**3 - 8*x + 1

def gradient_descent(start_x, lr=0.01, epochs=100):
    x = start_x
    for _ in range(epochs):
        grad = gradient(x)
        x = x - lr * grad
    return x

if __name__ == "__main__":
    # Thả viên bi ở bên phải sườn núi
    diem_1 = gradient_descent(start_x=3.0)
    
    # Thả viên bi ở bên trái sườn núi
    diem_2 = gradient_descent(start_x=-3.0)
    
    logging.info(f"Thả bi từ x=3.0, AI trôi về đáy ở vị trí: x = {diem_1:.4f} (Global Minimum)")
    logging.info(f"Thả bi từ x=-3.0, AI trôi về đáy ở vị trí: x = {diem_2:.4f} (Local Minimum - Bị kẹt!)")

```
### 🧠 Vũ khí mới: Gradient Descent with Momentum

Thay vì chỉ đi theo độ dốc tại vị trí hiện tại (rất dễ bị dừng lại nếu đáy phẳng), ta sẽ cho viên bi tích lũy **Vận tốc ($v$)** từ những bước đi trước.

* Nếu viên bi đang lăn xuống dốc cực nhanh, nó sẽ có một cái "đà" rất lớn.
* Khi chạm tới cái đáy giả (Local Minima), dù độ dốc lúc này bằng $0$, nhưng nhờ cái "đà" tích lũy được, viên bi sẽ vọt thẳng qua ngọn đồi nhỏ phía trước để đi tìm cái đáy sâu hơn!

**Công thức Toán học (Cập nhật 2 bước):**

1. Cập nhật vận tốc: 
$$v = \gamma \cdot v + \alpha \cdot \nabla f(x)$$


2. Cập nhật vị trí: 
$$x = x - v$$



*(Trong đó: $\alpha$ là Learning Rate, $\gamma$ (Gamma) là hệ số bảo toàn quán tính - thường đặt là $0.9$)*

---

### 🎮 Nhiệm Vụ Của Bro: Vượt Ngục Local Minima

Dưới đây là hàm Non-convex $f(x) = x^4 - 4x^2 + x$ mà chúng ta vừa khảo sát. Lần trước thả bi ở $x = 3.0$, nó đã bị kẹt ở đáy phụ $x \approx 1.31$.

Lần này, bro hãy hoàn thiện thuật toán Momentum để xem nó có phá vỡ được gông cùm không nhé!

**Yêu cầu:**
Copy đoạn code dưới đây vào IDE. Điền đúng 2 dòng logic cập nhật `v` và `x` vào chỗ có chữ `TODO`.

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

def gradient(x: float) -> float:
    """Đạo hàm của hàm f(x) = x^4 - 4x^2 + x"""
    return 4 * x**3 - 8 * x + 1

def gradient_descent_momentum(start_x: float, lr: float = 0.01, gamma: float = 0.9, epochs: int = 100):
    x = start_x
    v = 0.0  # Vận tốc ban đầu bằng 0
    
    for step in range(epochs):
        grad = gradient(x)
        
        # ==========================================
        # TODO: Viết 2 dòng code toán học cập nhật Momentum vào đây
        # 1. Tính vận tốc mới (v)
        # 2. Tính vị trí mới (x)
        # ==========================================
        
        
    return x

if __name__ == "__main__":
    # Điểm xuất phát "tử thần" x = 3.0
    diem_cuoi = gradient_descent_momentum(start_x=3.0)
    
    logging.info(" KẾT QUẢ THỬ NGHIỆM MOMENTUM:")
    logging.info(f"Vị trí bi dừng lại: x = {diem_cuoi:.4f}")
    
    if diem_cuoi < 0:
        logging.info(" THÀNH CÔNG! Viên bi đã vọt qua đồi và tìm thấy Global Minimum (khoảng -1.44)!")
    else:
        logging.info(" THẤT BẠI! Viên bi vẫn bị kẹt ở Local Minimum (khoảng 1.31). Kiểm tra lại code nhé!")

```
