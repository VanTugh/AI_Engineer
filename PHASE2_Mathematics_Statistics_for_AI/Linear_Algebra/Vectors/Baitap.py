import numpy as np
import logging

# Áp dụng Logging của Phase 1
logging.basicConfig(level=logging.INFO, format="%(message)s")
def compute_cosine_similarity(v1: np.ndarray, v2: np.ndarray) -> float:
    """Tính toán Cosine Similarity giữa 2 vector"""
    # Tính tích vô hướng và độ dài
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    # Áp dụng bẫy lỗi chia cho 0 bằng lệnh if (gọn hơn try/except)
    if norm_v1 == 0 or norm_v2 == 0:
        logging.warning("⚠️ Cảnh báo: Vector có độ dài bằng 0, không thể tính góc!")
        return 0.0
    # Tính Cosine
    cosine = dot_product / (norm_v1 * norm_v2)
    return float(cosine)
if __name__ == "__main__":
    # Khởi tạo dữ liệu
    word_apple = np.array([3, 4])
    word_banana = np.array([4, 3])
    word_car = np.array([-4, 3])
    # Tính toán
    sim_apple_banana = compute_cosine_similarity(word_apple, word_banana)
    sim_apple_car = compute_cosine_similarity(word_apple, word_car)
    # In kết quả chuẩn AI Engineer
    logging.info(f"(Apple - Banana) Cosine Score: {sim_apple_banana:.4f}")
    logging.info(f"(Apple - Car) Cosine Score: {sim_apple_car:.4f}")
    # Phân tích kết quả toán học
    if sim_apple_banana > 0.8:
        logging.info(
            "Nhận xét: Táo và Chuối có điểm cosine rất cao, chúng có nét nghĩa tương đồng (Đều là trái cây).")
    if np.isclose(sim_apple_car, 0):  # Dùng np.isclose thay vì == 0 để tránh lỗi làm tròn số thập phân của máy tính
        logging.info(
            "Nhận xét: Táo và Xe hơi có điểm cosine bằng 0. Hai vector này TRỰC GIAO (Orthogonal). Chúng không liên quan gì đến nhau!")