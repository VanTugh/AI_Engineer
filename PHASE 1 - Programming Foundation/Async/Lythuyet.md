### 1. Bản chất của `async / await` và Event Loop
Hãy tưởng tượng bro ra quán Highlands:

* **Sync (Đồng bộ):** Bro order cafe, đứng ỳ tại quầy chờ nhân viên pha xong, lấy ly cafe rồi mới về bàn. Người phía sau phải đợi bro xong mới được order. (Ứng dụng bị treo).
* **Async (Bất đồng bộ):** Bro order, nhân viên đưa cho cái thẻ rung (`await`). Bro về bàn lướt điện thoại (chương trình làm việc khác). Khi nào thẻ rung, bro ra lấy nước. **Event Loop** chính là cái hệ thống thẻ rung điều phối mọi việc sau lưng.

*Cú pháp:* Thay vì `def`, ta dùng `async def`. Thay vì gọi hàm bình thường, ta phải có chữ `await` ở trước.

```python
import asyncio

async def fetch_data():
    # await báo hiệu: "Chỗ này tốn thời gian đấy, Event Loop đi làm việc khác đi!"
    await asyncio.sleep(2) 
    return "Data hoàn tất"

```

### 2. Sát thủ gọi API: `httpx` vs `aiohttp`

* **`aiohttp`**: Là lão làng trong việc gọi HTTP bất đồng bộ, nhưng cú pháp hơi rườm rà.
* **`httpx` (Khuyên dùng)**: Đây là chân ái hiện tại của anh em AI Engineer. Cú pháp của nó giống hệt thư viện `requests` huyền thoại nhưng hỗ trợ chuẩn `async`. Khi làm dự án thực tế, các SDK như OpenAI hay LangChain đều dùng `httpx` ở dưới nền.

### 3. Thuật phân thân: `asyncio.gather()`

Đây là "bảo bối" khi bro làm Multi-LLM Orchestration (Phase 7).
Giả sử bro cần gọi 3 model: GPT-4 (mất 2s), Claude (mất 3s), Gemini (mất 1s).

* Nếu gọi tuần tự: Tổng thời gian = 2 + 3 + 1 = **6 giây**.
* Nếu dùng `asyncio.gather()` để gọi đồng loạt: Cả 3 request xuất phát cùng lúc. Tổng thời gian chỉ bằng thời gian của thằng chậm nhất = **3 giây**. Tốc độ tăng gấp đôi!

### 4. Streaming LLM Responses (Hiệu ứng gõ chữ)

Bro có nhớ tính năng `yield` (Generators) ở phần 1.7 để tiết kiệm RAM không? Khi ghép `async` với `yield`, chúng ta tạo ra `AsyncGenerator`.
Thay vì chờ LLM sinh xong nguyên bài văn 1000 chữ (mất 15s) rồi mới hiện ra, ta sẽ dùng `async for` để "hứng" từng từ khóa (token) ngay khi nó vừa được nhả ra khỏi server. Đó chính là bí mật đằng sau hiệu ứng gõ chữ mượt mà của ChatGPT.

---

### 🎮 Bài Tập Thực Chiến: Trận Chiến Đa Vũ Trụ (Multi-API Caller)

Đây chính là Project mức **Medium 🟡** mà Roadmap đã đề cập. Bro hãy mô phỏng việc gọi 3 model AI cùng một lúc.

*(Lưu ý: Chúng ta không dùng API thật để tránh rườm rà lộ Key, mà dùng `asyncio.sleep` để giả lập độ trễ của mạng).*

**Khung code có sẵn:**

```python
import asyncio
import time

async def call_mock_api(model_name: str, delay: int) -> str:
    """Hàm giả lập việc gọi API của một model AI"""
    print(f"🚀 [{model_name}] Bắt đầu gọi API...")
    await asyncio.sleep(delay) # Giả lập thời gian chờ server xử lý
    print(f"✅ [{model_name}] Đã sinh xong text!")
    return f"Kết quả siêu việt từ {model_name}"

async def main():
    start_time = time.time()
    
    # YÊU CẦU CỦA BRO Ở ĐÂY:
    # 1. Hãy tạo ra 3 tasks gọi hàm call_mock_api cho:
    #    - "GPT-4" (độ trễ 2 giây)
    #    - "Claude-3.5" (độ trễ 3 giây)
    #    - "Gemini-1.5" (độ trễ 1 giây)
    # 2. Dùng asyncio.gather() để chạy cả 3 tasks này CÙNG MỘT LÚC và lấy kết quả.
    # 3. In mảng kết quả ra màn hình.
    
    # Code của bro:
    # results = await ...
    
    end_time = time.time()
    print(f"⏱️ Tổng thời gian chạy: {end_time - start_time:.2f} giây")

# Dòng này để khởi động Event Loop (Không cần sửa)
if __name__ == "__main__":
    asyncio.run(main())

```

**Nhiệm vụ:**
Bro hãy hoàn thiện hàm `main()`. Nếu bro code đúng, tổng thời gian in ra ở cuối sẽ xấp xỉ **3.00 giây** chứ không phải 6 giây.
