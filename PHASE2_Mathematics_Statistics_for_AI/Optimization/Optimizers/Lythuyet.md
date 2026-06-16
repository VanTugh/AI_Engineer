### 1. RMSProp: Hệ thống Phanh tự động

Nếu Momentum là "chân ga", thì RMSProp (Root Mean Square Propagation) chính là "chân phanh" độc lập cho từng bánh xe.

* **Bản chất:** Trong Mạng Nơ-ron có hàng triệu trọng số (Weights). Có cái thì đạo hàm siêu to (dốc đứng), có cái đạo hàm siêu nhỏ (bằng phẳng). Dùng chung một mức Learning Rate ($\alpha$) là tự sát!
* **Cách hoạt động:** RMSProp tính **trung bình cộng bình phương của các gradient trong quá khứ** ($v$).
* Nếu một hướng đi đang có độ dốc quá gắt $\implies$ $v$ sẽ rất lớn $\implies$ Nó lấy Learning Rate CHIA cho $\sqrt{v}$ để đạp phanh, hãm tốc độ lại.
* Nếu hướng đi bằng phẳng $\implies$ $v$ nhỏ $\implies$ Phép chia làm Learning Rate TĂNG lên, giúp AI tăng tốc vượt qua vùng đất bằng.


* **Công thức lõi:** 
$$v_t = \beta \cdot v_{t-1} + (1-\beta) \cdot g_t^2$$


$$\theta = \theta - \frac{\alpha}{\sqrt{v_t} + \epsilon} \cdot g_t$$



### 2. Adam Optimizer: Vị Vua Không Ngai (Momentum + RMSProp)

Adam (Adaptive Moment Estimation) là sự kết hợp hoàn hảo. Vừa có "Quán tính" để lăn nhanh (Tử số), vừa có "Phanh tự động" để không bị lật xe (Mẫu số). Hầu hết các paper Deep Learning hiện nay đều xài Adam làm mặc định.

**5 Phương trình cấu thành nên Adam:**

1. Cập nhật Quán tính (Momentum): 
$$m_t = \beta_1 \cdot m_{t-1} + (1 - \beta_1) \cdot g_t$$


2. Cập nhật Phanh (RMSProp): 
$$v_t = \beta_2 \cdot v_{t-1} + (1 - \beta_2) \cdot g_t^2$$


3. *Bias Correction (Sửa lỗi khởi động chậm cho $m$):* 
$$\hat{m}_t = \frac{m_t}{1 - \beta_1^t}$$


4. *Bias Correction (Sửa lỗi khởi động chậm cho $v$):* 
$$\hat{v}_t = \frac{v_t}{1 - \beta_2^t}$$


5. Cập nhật Trọng số: 
$$\theta = \theta - \frac{\alpha}{\sqrt{\hat{v}_t} + \epsilon} \cdot \hat{m}_t$$



### 3. Learning Rate Schedules (Nghệ thuật sang số)

Ngay cả khi có Adam, việc giữ Learning Rate cố định từ đầu đến cuối là một sai lầm. Khi mới train, mô hình cần bước đi lớn để khám phá. Khi sắp tới đích, nó cần đi chậm lại li ti để rơi trúng tâm của cái đáy (không bị dao động quanh mép).

* **Step Decay:** Đơn giản và cục súc. Cứ sau $N$ epoch, chặt đôi Learning Rate. Đồ thị trông như bậc thang.
* **Cosine Annealing:** Mượt mà hơn. Learning Rate giảm dần theo đường cong lượn sóng của hàm Cosine, giúp mô hình lướt êm ái về đích.
* **Warmup (Khởi động nóng):** Linh hồn của các mô hình LLMs (như ChatGPT). Khởi đầu, AI hoàn toàn "mù tịt" nên rất dễ tính ra gradient sai lệch. Nếu để LR cao ngay lúc đầu, nó sẽ văng mất xác (Divergence). Vì vậy, LR sẽ bắt đầu từ $0$, **tăng dần** lên mức đỉnh trong vài epoch đầu, rồi mới bắt đầu giảm xuống (Decay).

---

### 🔥 BÀI TẬP TRY HARD: CÀI ĐẶT TRÁI TIM CỦA ADAM OPTIMIZER

Khi bro gọi `torch.optim.Adam()`, đằng sau nó chính là một vòng lặp chạy 5 phương trình toán học ở trên. Bây giờ, bro hãy tự tay code lại cơ chế cập nhật này bằng NumPy!

**Bối cảnh:** Mô hình đã chạy xong Forward Pass và Backward Pass, lấy ra được Gradient của vòng lặp hiện tại (Bước $t$). Bro phải viết hàm cập nhật Trọng số (Weights) theo chuẩn thuật toán Adam.

**Nhiệm vụ của Intern:**
Hoàn thiện 5 dòng code toán học bên dưới chỗ `TODO`. Nhớ dùng đúng các phép tính Vector của NumPy (ví dụ: ` 2` cho bình phương, `np.sqrt()` cho căn bậc 2).

```python
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

def adam_step(theta: np.ndarray, grad: np.ndarray, m: np.ndarray, v: np.ndarray, t: int, 
              lr: float = 0.01, beta1: float = 0.9, beta2: float = 0.999, epsilon: float = 1e-8):
    """
    Thực hiện 1 bước cập nhật trọng số bằng thuật toán Adam.
    Các tham số:
    - theta: Trọng số hiện tại
    - grad: Đạo hàm (Gradient) tại bước t
    - m, v: Các biến trạng thái lưu quán tính và phanh từ bước trước
    - t: Bước hiện tại (Epoch / Iteration hiện tại, bắt đầu từ 1)
    """
    
    # =======================================================
    # TODO: TRY HARD MODE - CHUYỂN TOÁN HỌC THÀNH CODE NUMPY
    # =======================================================
    
    # 1. Cập nhật Momentum (m_t)
    # m = ...
    
    # 2. Cập nhật RMSProp (v_t)
    # v = ...
    
    # 3. Bias Correction cho m (m_hat)
    # m_hat = ...
    
    # 4. Bias Correction cho v (v_hat)
    # v_hat = ...
    
    # 5. Cập nhật Trọng số (theta)
    # theta = ...
    
    # =======================================================
    
    return theta, m, v

if __name__ == "__main__":
    # Test case cực gắt để kiểm tra logic
    theta_test = np.array([1.0, -0.5])
    grad_test = np.array([0.1, -0.2])
    m_test = np.array([0.0, 0.0])
    v_test = np.array([0.0, 0.0])
    
    theta_new, m_new, v_new = adam_step(theta_test, grad_test, m_test, v_test, t=1)
    
    # Kết quả kỳ vọng sau bước 1:
    # m_hat xấp xỉ grad, v_hat xấp xỉ grad^2
    # Do đó m_hat / sqrt(v_hat) sẽ làm cho bước nhảy xấp xỉ 1.0 hoặc -1.0
    # Với lr = 0.01, theta mới sẽ bị trừ đi một lượng xấp xỉ 0.01 theo dấu của gradient
    
    logging.info("Trọng số cũ: " + str(theta_test))
    logging.info("Trọng số mới (Adam): " + str(theta_new))
    
    # Nếu code chuẩn, theta_new[0] phải giảm (vì grad dương), theta_new[1] phải tăng (vì grad âm).
    if theta_new[0] < theta_test[0] and theta_new[1] > theta_test[1]:
        logging.info("🔥 BÁ ĐẠO! Bro đã tự tay cài đặt xong Adam Optimizer!")
    else:
        logging.info("❌ Sai hướng rồi! Kiểm tra lại công thức toán học nhé.")

```