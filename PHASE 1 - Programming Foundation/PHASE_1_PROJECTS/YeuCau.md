
---

### 🟢 Project 1 (Easy): Python AI Toolkit CLI

**📝 Dịch yêu cầu:**
Xây dựng một công cụ dòng lệnh (CLI tool) nhận đầu vào là văn bản và gọi OpenAI API.

* **Tính năng:** Tóm tắt văn bản, Dịch thuật, Phân tích cảm xúc (vui/buồn/tức giận).
* **Công nghệ:** Python, `argparse` (để nhận lệnh từ terminal), `openai` SDK, `.env` (để bảo mật API Key).

**💡 Gợi ý thiết kế (Hints):**

1. **File cấu trúc:** Cần file `.env` chứa `OPENAI_API_KEY` và file `cli.py`.
2. **Argparse Setup:** Bro cần dùng `argparse` để người dùng có thể gõ trên terminal kiểu:
`python cli.py --text "Hôm nay tôi rất vui" --action sentiment`
*(Cần thiết lập tham số `--text` nhận chuỗi và `--action` với các lựa chọn: `summarize`, `translate`, `sentiment`)*.
3. **Xử lý API:** Viết một hàm `call_openai(text, action)`.
* Dùng `if/elif` (Routing) để đổi System Prompt tương ứng với cái `action` mà người dùng chọn.
* *Mẹo:* Nếu bro chưa có API Key của OpenAI hoặc không muốn tốn tiền thật, hãy viết một hàm *giả lập* (Mock API) trả về kết quả dựa trên action, nhưng **phải giữ nguyên cấu trúc code** như thể đang gọi thư viện OpenAI thật nhé.



---

### 🟡 Project 2 (Medium): Async Multi-API Caller

**📝 Dịch yêu cầu:**
Gọi 3 mô hình (OpenAI, Anthropic, Gemini) **cùng một lúc** bằng `asyncio.gather()`. So sánh các câu trả lời cạnh nhau trên terminal. Thêm tính năng bắt lỗi mạng và thử lại với thời gian chờ tăng dần (exponential backoff).

* **Công nghệ:** Python, `httpx` (để gọi mạng bất đồng bộ), `asyncio`, thư viện `rich` (để in bảng đẹp ra terminal).

**💡 Gợi ý thiết kế (Hints):**

1. **Exponential Backoff (Thử lại tăng dần):** Đây là kỹ năng siêu quan trọng. Thay vì gọi lại ngay lập tức khi lỗi, bro cho vòng lặp nghỉ `1s`, nếu vẫn lỗi thì nghỉ `2s`, rồi `4s`, tối đa 3 lần. (Dùng `while` loop + `try/except` + `asyncio.sleep`).
2. **Thư viện Rich:** Cài `pip install rich`. Bro dùng `Table` và `Console` của thư viện này để in 3 kết quả thành 3 cột nhìn cho ngầu.
3. **Mock API (Nâng cao):** Tương tự Project 1, bro có thể tự viết hàm giả lập `httpx.AsyncClient().get()`, nhưng cố tình dùng `random` để thi thoảng ném ra một cái lỗi `TimeoutError` nhằm test xem cái luồng Backoff của bro có hoạt động không.

---

### 🔴 Project 3 (Hard): Production-Grade Data Pipeline

**📝 Dịch yêu cầu:**
Xây dựng một luồng xử lý dữ liệu chuẩn doanh nghiệp: Đọc file CSV, làm sạch dữ liệu rác, băm nhỏ dữ liệu thành các lô (batches), và gửi tới API Embedding (nhúng văn bản thành vector) của OpenAI.

* **Tính năng:** Có thanh tiến trình chạy, có khả năng phục hồi lỗi (Error recovery), có khả năng chạy tiếp từ chỗ bị đứt (Resume from checkpoint), xử lý lô bất đồng bộ.
* **Công nghệ:** Pandas, NumPy, `tqdm`, `asyncio`, OpenAI Embeddings.

**💡 Gợi ý thiết kế (Hints):**

1. **Pandas Clean:** Dùng `dropna()` hoặc `fillna()` để dọn file CSV thô.
2. **Async Batching:** Dùng generator (`yield`) để cắt CSV thành các chunk (VD: 100 dòng/lô). Đẩy các lô này vào `asyncio.gather`.
3. **Checkpoint (Linh hồn của bài này):** Sau khi gửi xong lô thứ `N`, bro dùng `json.dump` ghi số `N` này vào một file `checkpoint.json`. Nếu luồng bị sập ở lô `N+1`, lần chạy sau code phải đọc file json này và bắt đầu xử lý từ lô `N+1` chứ không chạy lại từ lô số 0.

---
