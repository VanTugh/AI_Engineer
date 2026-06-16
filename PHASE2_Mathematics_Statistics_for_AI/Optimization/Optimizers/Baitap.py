import numpy as np
import logging

from pandas import bdate_range

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

    # 1. Cập nhật Momentum (m_t)
    m = beta1 * m + (1 - beta1) * grad

    # 2. Cập nhật RMSProp (v_t)
    v = beta2 * v + (1 - beta2) * grad**2

    # 3. Bias Correction cho m (m_hat)
    m_hat = m / (1 - beta1 ** t)

    # 4. Bias Correction cho v (v_hat)
    v_hat = v / (1 - beta2 ** t)

    # 5. Cập nhật Trọng số (theta)
    theta = theta - (lr / (np.sqrt(v_hat) + epsilon) * m_hat)

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
        logging.info("BÁ ĐẠO! Bro đã tự tay cài đặt xong Adam Optimizer!")
    else:
        logging.info("Sai hướng rồi! Kiểm tra lại công thức toán học nhé.")