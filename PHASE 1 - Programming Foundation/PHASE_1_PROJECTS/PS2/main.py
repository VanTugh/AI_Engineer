import asyncio
import time
from unittest import result


async def call_mock_api(model_name: str, delay: int) -> str:
    """Hàm giả lập việc gọi API của một model AI"""
    print(f" [{model_name}] Bắt đầu gọi API...")
    await asyncio.sleep(delay)  # Giả lập thời gian chờ server xử lý
    print(f"[{model_name}] Đã sinh xong text!")
    return f"Kết quả siêu việt từ {model_name}"


async def main():
    start_time = time.time()

    # YÊU CẦU CỦA BRO Ở ĐÂY:
    # 1. Hãy tạo ra 3 tasks gọi hàm call_mock_api cho:
    #    - "GPT-4" (độ trễ 2 giây)
    #    - "Claude-3.5" (độ trễ 3 giây)
    #    - "Gemini-1.5" (độ trễ 1 giây)
    model_name_1 = "GPT-4"
    model_name_2 = "Claude-3.5"
    model_name_3 = "Gemini-1.5"
    # 2. Dùng asyncio.gather() để chạy cả 3 tasks này CÙNG MỘT LÚC và lấy kết quả.
    result = await asyncio.gather(
        call_mock_api(model_name_1, 2),
        call_mock_api(model_name_2, 3),
        call_mock_api(model_name_3, 1)
    )
    # 3. In mảng kết quả ra màn hình.
    print("Ket qua")
    print(result)
    end_time = time.time()
    print(f"Tổng thời gian chạy: {end_time - start_time:.2f} giây")
# Dòng này để khởi động Event Loop (Không cần sửa)
if __name__ == "__main__":
    asyncio.run(main())