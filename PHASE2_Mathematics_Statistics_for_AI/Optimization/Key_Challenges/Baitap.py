import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")


def clip_gradients_l2(grad: np.ndarray, max_norm: float = 1.0) -> np.ndarray:
    """
    Cắt xén vector đạo hàm để chống hiện tượng Exploding Gradient.
    Vẫn giữ nguyên 'hướng' của vector, chỉ thu nhỏ 'độ lớn' (magnitude).
    """

    # ==========================================
    # TODO: Viết code Gradient Clipping vào đây
    # 1. Tính L2 Norm của grad
    L2_norm = np.linalg.norm(grad)
    # 2. Kiểm tra và scale lại grad nếu vượt max_norm
    # ==========================================
    if L2_norm > max_norm:
        grad= grad_exploded * (max_norm / L2_norm)
    return grad


if __name__ == "__main__":
    # Vector đạo hàm đang bị bùng nổ
    grad_exploded = np.array([100.0, -500.0, 1000.0])

    logging.info("💣 Gradient trước khi clip: " + str(grad_exploded))
    logging.info("Độ lớn (Norm) ban đầu: " + str(np.linalg.norm(grad_exploded)))
    logging.info("-" * 40)

    # Kích hoạt cầu dao với max_norm = 1.0
    grad_safe = clip_gradients_l2(grad_exploded, max_norm=1.0)

    logging.info("Gradient sau khi clip: " + str(grad_safe))
    logging.info("Độ lớn (Norm) lúc sau: " + str(np.linalg.norm(grad_safe)))

    # Kiểm tra tỷ lệ hướng đi (Phải được giữ nguyên)
    ty_le_truoc = grad_exploded[2] / grad_exploded[0]  # 1000 / 100 = 10
    ty_le_sau = grad_safe[2] / grad_safe[0]

    if np.isclose(ty_le_truoc, ty_le_sau) and np.linalg.norm(grad_safe) <= 1.0001:
        logging.info("HOÀN HẢO! Cầu dao đã ngắt đúng lúc, AI được cứu sống!")
    else:
        logging.info("Cháy máy rồi! Kiểm tra lại công thức scale nhé.")