import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Giả lập ma trận dữ liệu (100 dòng, 50 cột)
# Để mô phỏng dữ liệu có tính quy luật, ta tạo một ma trận Rank thấp (Rank = 5) rồi cộng thêm chút nhiễu
np.random.seed(42)
hidden_factors = np.random.randn(100, 5)
weights = np.random.randn(5, 50)
noise = np.random.randn(100, 50) * 0.1

X_original = hidden_factors @ weights + noise
def compress_data_svd(X: np.ndarray, k: int) -> np.ndarray:
    U, S, Vt = np.linalg.svd(X, full_matrices=False)
    S_new = np.diag(S[:k])
    U_new = U[:,:k]
    Vt_new = Vt[:k,:]
    X_recovered = U_new @ S_new @ Vt_new
    return X_recovered

if __name__ == "__main__":
    k =5
    X_reconstructed = compress_data_svd(X_original, k)

    # Tính sai số (Khoảng cách L2 giữa ma trận gốc và ma trận phục hồi)
    error = np.linalg.norm(X_original - X_reconstructed)

    logging.info(f"Kích thước ma trận gốc: {X_original.shape}")
    logging.info(f"Kích thước ma trận sau khi phục hồi: {X_reconstructed.shape}")
    logging.info("-" * 40)
    logging.info(f"Sai số phục hồi (Reconstruction Error) với k={k}: {error:.4f}")