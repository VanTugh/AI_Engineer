import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def call_llm_api(prompt):
    # Hàm này mô phỏng môi trường bị lỗi, chỉ ném lỗi ra ngoài
    raise ValueError("API Key đã hết tiền!")


if __name__ == "__main__":
    logging.info("Bắt đầu chương trình.")

    # Nơi GỌI hàm sẽ là nơi BẪY lỗi
    try:
        # Cố gắng gọi hàm
        response = call_llm_api("Xin chào")
        logging.info(f"Kết quả từ API: {response}")

    except ValueError as e:
        # Hứng đúng cái lỗi ValueError văng ra từ bên trong hàm
        logging.error(f"Lỗi khi gọi API: {e}")

    finally:
        # Dọn dẹp chiến trường
        logging.info("Đóng luồng kết nối API.")