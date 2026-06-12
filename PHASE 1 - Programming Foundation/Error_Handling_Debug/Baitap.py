import logging

# 1. Cấu hình logging mức INFO
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def call_llm_api(prompt):
    # Giả lập lỗi API
    raise ValueError("API Key đã hết tiền!")

try:
    response = call_llm_api("Xin chào")
    logging.info(f"Kết quả từ API: {response}")

# 2. Bẫy lỗi ValueError
except ValueError as e:
    # 3. Ghi nhận lỗi bằng logging.error
    logging.error(f"Lỗi khi gọi API: {e}")

finally:
    # 4. Luôn thực thi dù có lỗi hay không
    logging.info("Đóng luồng kết nối API.")