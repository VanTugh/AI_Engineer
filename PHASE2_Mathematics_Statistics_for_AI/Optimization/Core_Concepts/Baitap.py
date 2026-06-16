import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def gradient(x: float) -> float:
    """Đạo hàm của hàm f(x) = x^4 - 4x^2 + x"""
    return 4 * x ** 3 - 8 * x + 1


def gradient_descent_momentum(start_x: float, lr: float = 0.01, gamma: float = 0.9, epochs: int = 100):
    x = start_x
    v = 0.0  # Vận tốc ban đầu bằng 0

    for step in range(epochs):
        grad = gradient(x)

        # ==========================================
        # TODO: Viết 2 dòng code toán học cập nhật Momentum vào đây
        v = gamma * v + lr * grad
        x = x - v
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
