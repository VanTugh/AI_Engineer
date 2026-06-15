import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-x))


def sigmoid_derivative(x: np.ndarray) -> np.ndarray:
    return sigmoid(x) * (1 - sigmoid(x))


if __name__ == "__main__":
    x = np.array([-1.0, 0.0, 1.0])

    # Kích hoạt sức mạnh Vectorization của Numpy (Không dùng vòng lặp)
    derivatives = sigmoid_derivative(x)

    logging.info(f"Giá trị đạo hàm tại các điểm {x} lần lượt là:\n{derivatives}")
    logging.info(f"Độ dốc lớn nhất đạt được: {np.max(derivatives)}")