import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# X = [Bias (1), Số phòng, Diện tích]
X = np.array([
    [1, 2, 50],
    [1, 3, 75],
    [1, 4, 100],
    [1, 3, 85],
    [1, 5, 120]
])

# Giá nhà tương ứng (tỷ VNĐ)
y = np.array([3.0, 4.5, 6.0, 5.0, 7.5])
def train_linear_regression(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    W = np.linalg.inv(X.T @ X)@X.T @ y
    return W
if __name__ == '__main__':
    W = train_linear_regression(X, y)
    logging.info("W = {}".format(W))