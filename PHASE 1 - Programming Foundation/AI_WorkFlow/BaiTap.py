import os
from dotenv import load_dotenv
from tqdm import tqdm
import time

# Nạp các biến môi trường từ file .env
load_dotenv()

# Lấy giá trị SECRET_TOKEN
API_SECRET = os.getenv("SECRET_TOKEN")

# Kiểm tra xem đã lấy được chưa
print("SECRET_TOKEN =", API_SECRET)

# Thanh tiến trình chạy 10 lần
for i in tqdm(range(10), desc="Đang xử lý"):
    time.sleep(0.2)

print("Hoàn thành!")