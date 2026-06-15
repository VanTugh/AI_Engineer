import logging
logging.basicConfig(level=logging.INFO, format='%(message)s')
def train_gradient_descent(x_start: float, lr: float, epochs: int):
    x = x_start
    tolerance = 1e-6

    logging.info(f" Bắt đầu thả máy tính rơi từ đỉnh núi x = {x:.2f}")
    for step in range(1, epochs + 1):
        gradient = 2 * x
        loss = x ** 2
        x = x - lr * gradient
        logging.info(f"Epoch {step:02d}/{epochs} | Vị trí x = {x:.6f} | Gradient = {gradient:.6f} | Loss = {loss:.6f}")
        if abs(gradient) < tolerance:
            logging.info(f" Đã chạm đáy thung lũng ở Epoch {step}. Dừng sớm để tiết kiệm điện!")
            break
if __name__ == "__main__":
    train_gradient_descent(x_start=5.0, lr=0.1, epochs=20)