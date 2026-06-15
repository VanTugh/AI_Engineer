import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def relu(x: np.ndarray) -> np.ndarray:
    """Hàm kích hoạt ReLU (Lan truyền xuôi)"""
    return np.maximum(0, x)


def relu_derivative(x: np.ndarray) -> np.ndarray:
    """Đạo hàm ReLU (Lan truyền ngược)"""
    # Nhân với 1.0 để biến True thành 1.0, False thành 0.0
    return (x > 0) * 1.0


if __name__ == '__main__':
    x = np.array([-2.5, 0.0, 3.1, -1.0, 5.5])
    out = relu(x)
    logging.info(f" Kết quả sau khi qua ReLU:\n{out}")
    grad = relu_derivative(x)
    logging.info(f" Đạo hàm (Gradient) tại các điểm x:\n{grad}")