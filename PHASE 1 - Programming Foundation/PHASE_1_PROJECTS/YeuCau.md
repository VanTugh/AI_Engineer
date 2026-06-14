
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
---

### Bước 1: Tư duy Hộp đen (Black-Box Thinking) - Xác định Input/Output

Đừng lao vào nghĩ đến thuật toán vội. Hãy nhìn hệ thống như một cái hộp đen.

* **Input của hệ thống là gì?** File CSV (rất nhiều rác, có thể có dòng bị lỗi).
* **Output cần đạt được là gì?** Toàn bộ text được nhúng thành Vector một cách an toàn.
* **Ràng buộc (Constraints):** * API của OpenAI gọi quá nhanh sẽ bị khóa (Rate Limit).
* Giữa chừng rớt mạng thì sao? (Phải có Checkpoint).



### Bước 2: Vẽ Luồng dữ liệu (Data Flow)

Bro cần tưởng tượng đường đi của dữ liệu từ lúc là file thô đến lúc thành thành phẩm. Tôi thường lấy giấy bút ra vạch 4 trạm dừng:
`CSV Thô` ➡️ `Làm sạch (Pandas)` ➡️ `Băm nhỏ (Chunker)` ➡️ `Gửi API (Async)` ➡️ `Lưu trạng thái (JSON)`

### Bước 3: Tư duy "Chia để trị" (Modular Design)

Hệ thống lớn dễ gãy. Phải băm nó thành các module nhỏ, độc lập. Ở bài 3, tôi thiết kế theo 4 khối:

1. **Khối Tiền xử lý (`tien_xu_ly`):** Nhiệm vụ duy nhất là nhận đường dẫn file và nhả ra một List sạch. Không cần biết API là cái gì.
2. **Khối Chia lô (`chunker`):** Chỉ làm đúng việc thái thịt. Đưa cục bự, nhả cục nhỏ.
3. **Khối Bộ nhớ (`save/load_checkpoint`):** Chỉ làm việc với ổ cứng.
4. **Khối Động cơ (`process_pipeline`):** Đây là "bộ não", gọi các khối kia lên ráp lại với nhau.

*Tại sao phải chia?* Vì lỡ sau này sếp bảo: *"Đổi cho anh từ đọc file CSV sang đọc từ Database SQL"*. Bro chỉ cần viết lại đúng khối 1, ba khối còn lại không cần đụng đến một chữ! Đó là thiết kế tốt.

### Bước 4: Tư duy Phòng thủ (Defensive Programming) - "Làm sao để nó sập?"

Đây là bước phân biệt Senior và Intern. Senior luôn nhìn đâu cũng thấy rủi ro.
Tôi sẽ tự đặt câu hỏi phản biện cho thiết kế của mình:

* *Hỏi:* Nếu file CSV có những khoảng trắng vô hình thì sao?
* *Giải quyết:* Phải thêm lệnh `.strip()` vào Pandas.


* *Hỏi:* Nếu chia lô 1000 câu/lần thì sao?
* *Giải quyết:* Bị quá tải (Timeout) mạng ngay. Phải dùng `batch_size` nhỏ thôi (ví dụ 5-10).


* *Hỏi:* Đang ghi file `checkpoint.json` dở tay thì sập nguồn, file bị rỗng (Bug bro vừa gặp) thì sao?
* *Giải quyết:* Phải có `try...except json.JSONDecodeError` để bắt lỗi khi đọc file rác.



### Bước 5: Viết code từ dưới lên (Bottom-up Implementation)

Khi đã có bản đồ trong đầu, bắt đầu mở IDE lên code. Nhưng nguyên tắc là: **Không code luồng chính ngay**.

* Viết hàm `tien_xu_ly` trước. Cho chạy thử in ra màn hình xem data có sạch không. Sạch rồi mới đi tiếp.
* Viết hàm `load/save checkpoint`. Chạy thử riêng nó xem có sinh ra file JSON không.
* Viết `mock_api`.
* Cuối cùng mới viết `process_pipeline` để nối các "viên gạch" đã được test kỹ lại với nhau.

---

