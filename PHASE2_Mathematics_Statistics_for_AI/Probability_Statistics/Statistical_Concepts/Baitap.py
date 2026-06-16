import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
label = np.array([0.0, 1.0, 0.0])
def cross_entropy_loss(P: np.ndarray, Q: np.ndarray) -> float:
    epsilon = 1e-15
    Q = np.clip(Q, epsilon, 1. - epsilon)  # Ép Q nằm trong khoảng an toàn
    loss = -np.sum(P * np.log(Q))
    return float(loss)
if __name__ == '__main__':
    predict_1 = np.array([0.1, 0.8, 0.1])
    loss_1 = cross_entropy_loss(label, predict_1)
    predict_2 = np.array([0.01, 0.98, 0.01])
    loss_2 = cross_entropy_loss(label, predict_2)

    logging.info(f"Loss khi tự tin 80%: {loss_1:.4f}")
    logging.info(f"Loss khi tự tin 98%: {loss_2:.4f}")
    logging.info("🎯 Sai số đã tụt dốc thê thảm khi AI thông minh hơn!")