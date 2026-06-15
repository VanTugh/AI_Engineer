import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
def compute_graph(x: float, y: float, z: float):
    q = x + y
    f = q * z
    logging.info(f" [FORWARD] Tính xuôi: q = {q}, f = {f}")
    grad_f = 1.0
    grad_z = q * grad_f
    grad_q = z * grad_f

    grad_x = 1.0 * grad_q
    grad_y = 1.0 * grad_q

    logging.info(f" [BACKWARD] Tính ngược (Gradients):")
    logging.info(f"   grad_z = {grad_z}")
    logging.info(f"   grad_x = {grad_x}")
    logging.info(f"   grad_y = {grad_y}")


if __name__ == '__main__':
    x = -2.0
    y = 5.0
    z = -4.0

    compute_graph(x, y, z)