import numpy as np
import logging
from dataclasses import dataclass
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

@dataclass
class LayerResult:
    output_matrix: np.ndarray
    weight_rank: int

def forward_pass(X: np.ndarray, W: np.ndarray, bias: np.ndarray) -> LayerResult:
    """Tính toán lớp mạng nơ-ron và trả về object LayerResult"""
    # Tính đầu ra Y
    Y = X @ W + bias
    rank = np.linalg.matrix_rank(W)
    return LayerResult(output_matrix=Y, weight_rank=rank)
if __name__ == '__main__':
    X = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
    W = np.array([[0.1, 0.2],
                  [0.3, 0.4],
                  [0.5, 0.6],
                  [0.7, 0.8]])
    bias = np.array([0.01, 0.02])
    result = forward_pass(X, W, bias)
    logging.info(f"Hạng (Rank) của ma trận Trọng số W: {result.weight_rank}")
    logging.info(f"Ma trận đầu ra Y:\n{result.output_matrix}")