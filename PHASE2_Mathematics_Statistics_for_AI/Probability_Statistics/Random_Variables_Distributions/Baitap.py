import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# Dữ liệu
hours_studied = np.array([1.0, 2.5, 3.0, 5.0, 7.5])
test_scores = np.array([40, 55, 65, 80, 95])

# Tính toán
kyvong_hours = np.mean(hours_studied)
kyvong_scores = np.mean(test_scores)
std_test_scores = np.std(test_scores)

# Dùng np.corrcoef và lấy giá trị ở hàng 0, cột 1 (so sánh hours_studied và test_scores)
correlation_matrix = np.corrcoef(hours_studied, test_scores)
correlation = correlation_matrix[0, 1]

# In log chuẩn AI Engineer
logging.info(f"Trung bình thời gian học: {kyvong_hours:.2f} giờ")
logging.info(f"Trung bình điểm số: {kyvong_scores:.2f} điểm")
logging.info(f"Độ lệch chuẩn của điểm: {std_test_scores:.2f} (Điểm dao động khá mạnh quanh mức trung bình)")
logging.info(f"Hệ số tương quan (Correlation): {correlation:.4f}")