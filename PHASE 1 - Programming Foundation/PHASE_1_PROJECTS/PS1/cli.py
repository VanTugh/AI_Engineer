import os
import logging
import argparse
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
load_dotenv()

def call_mock_openai(text: str, action: str):
    """Hàm giả lập gọi OpenAI API"""
    try:
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise ValueError("Không tìm thấy API_KEY trong môi trường!")

        logging.info("Đã tải API_KEY thành công (Đã giấu mã).")

        print("-" * 30)
        if action == "summarize":
            print(f" Đang tóm tắt: '{text}'")
            print("=> Kết quả: [Nội dung đã được tóm tắt cực ngắn]")

        elif action == "translate":
            print(f" Đang dịch: '{text}'")
            print("=> Kết quả: [English translation of the text]")

        elif action == "sentiment":
            print(f" Phân tích cảm xúc: '{text}'")
            print("=> Kết quả: [Tích cực - 99%]")

    except Exception as e:
        logging.error(f"Lỗi hệ thống: {e}")


def main():
    parser = argparse.ArgumentParser(description="Bộ công cụ AI CLI cực ngầu của AI Engineer")

    parser.add_argument(
        "--text",
        type=str,
        required=True,
        help="Đoạn văn bản bạn muốn AI xử lý"
    )

    parser.add_argument(
        "--action",
        type=str,
        required=True,
        choices=["summarize", "translate", "sentiment"],
        help="Hành động AI cần thực hiện"
    )

    args = parser.parse_args()
    call_mock_openai(args.text, args.action)
if __name__ == "__main__":
    main()

# Test chạy dịch thuật
# python cli.py --text "Bro code đỉnh quá" --action translate
#
# Test tính năng tự động nhắc lỗi của argparse (Cố tình gõ sai action)
# python cli.py --text "Test lỗi" --action code