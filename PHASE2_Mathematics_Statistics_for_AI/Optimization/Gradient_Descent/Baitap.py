import numpy as np
import logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
np.random.seed(42)
X_data = np.random.randn(1000, 3)
true_theta = np.array([[1.5], [-2.0], [3.0]])
y_data = X_data @ true_theta + np.random.randn(1000, 1) * 0.1
def mini_batch_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 50, batch_size: int = 32):
    m, n = X.shape
    theta = np.random.randn(n, 1)
    for epoch in range(epochs):
        # TODO 1: Shuffle dữ liệu ở đầu mỗi epoch
        indices = np.random.permutation(m)
        X_shuffled = X[indices, :]
        y_shuffled = y[indices, :]
        # Duyệt qua từng Mini-batch
        for i in range(0, m, batch_size):
            # TODO 2: Cắt lấy X_batch và y_batch (DÙNG BIẾN MỚI)
            X_batch = X_shuffled[i:i + batch_size, :]
            y_batch = y_shuffled[i:i + batch_size, :]
            # TODO 3: Tính y_hat
            y_hat = X_batch @ theta
            # TODO 4: Tính Gradient bằng Ma trận
            gd = (2 / batch_size) * (X_batch.T) @ (y_hat - y_batch)
            # TODO 5: Cập nhật trọng số
            theta = theta - lr * gd
    return theta
if __name__ == "__main__":
    logging.info("Trọng số thật sự:\n" + str(true_theta))
    logging.info("-" * 40)
    learned_theta = mini_batch_gd(X_data, y_data, lr=0.05, epochs=50, batch_size=64)
    logging.info("Trọng số AI học được:\n" + str(learned_theta))
    sai_so = np.linalg.norm(learned_theta - true_theta)
    if sai_so < 0.05:
        logging.info("QUÁ ĐỈNH! Mô hình đã hội tụ cực kỳ chính xác!")
    else:
        logging.info("Mô hình chưa hội tụ. Hãy kiểm tra lại công thức Gradient bằng Ma trận.")