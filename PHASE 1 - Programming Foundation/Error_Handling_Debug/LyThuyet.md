
### 1. `try / except / finally` và Bẫy lỗi cụ thể

Đừng bao giờ dùng `except:` chung chung (bare except), nó sẽ nuốt luôn cả lệnh dừng chương trình (Ctrl+C) của bro. Hãy bắt đúng cái lỗi bro nghi ngờ.

* **`try`**: Đổ code có nguy cơ sinh lỗi vào đây (vd: gọi API, đọc file, chia tensor).
* **`except SpecificError`**: Xử lý khi lỗi đúng loại đó xảy ra. Có thể nối nhiều block `except`.
* **`finally`**: Khối lệnh **LUÔN LUÔN CHẠY** dù có lỗi hay không. (Dùng để đóng kết nối database, đóng file, giải phóng RAM GPU).

```python
try:
    with open("data.json", "r") as f:
        data = json.load(f)
    result = 100 / len(data)
except FileNotFoundError:
    print("Không tìm thấy file dữ liệu!")
except ZeroDivisionError:
    print("Dữ liệu rỗng, không thể chia cho 0!")
finally:
    print("Đã hoàn tất luồng kiểm tra dữ liệu.")

```

### 2. Chủ động ném lỗi (`raise`) & Custom Exceptions

"Fail Fast" (Chết sớm còn hơn sống lay lắt). Nếu truyền data sai định dạng vào model, thà báo lỗi sập luôn từ đầu còn hơn là để model học ra cái kết quả rác.

* **`raise ValueError("Lỗi!")`**: Chủ động ngắt chương trình.
* **Custom Exception**: Tạo ra loại lỗi của riêng hệ thống AI của bro để dễ nhận diện.

```python
# Tạo ra một loại lỗi riêng biệt cho dự án
class ModelDivergedError(Exception): 
    pass

loss = 9999.99
if loss > 1000:
    # Ném lỗi ngay lập tức nếu mô hình học sai hướng
    raise ModelDivergedError(f"Loss quá cao ({loss}), model đã bị nổ gradient!") 

```

### 3. `logging` - Kẻ thay thế `print()` trong Production

Đi thực tập mà xài `print()` để log tiến trình train là mentor gõ đầu ngay. Khi code chạy trên server (ví dụ AWS hoặc Ubuntu server), không ai có màn hình để xem `print` cả. Tất cả phải ghi ra file bằng thư viện `logging`.

* **5 Cấp độ (Levels)**: `DEBUG` (chi tiết chạy code) < `INFO` (thông báo bình thường) < `WARNING` (cảnh báo, code vẫn chạy) < `ERROR` (lỗi cục bộ) < `CRITICAL` (lỗi chết app).

```python
import logging
# Cài đặt ghi log ra terminal (hoặc file) kèm thời gian
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Bắt đầu train epoch 1")
logging.warning("RAM GPU đang vượt quá 90%")
logging.error("Không tải được ảnh id_102.jpg")

```

### 4. Gỡ lỗi bằng `breakpoint()` và Đọc Traceback

* **Đọc Traceback (Lịch sử báo lỗi)**: Khi Python báo lỗi đỏ chót, nguyên tắc vàng là: **Đọc từ dưới lên trên**. Dòng cuối cùng cho biết "Lỗi gì", các dòng ngay trên nó chỉ ra "Lỗi ở file nào, dòng số mấy".
* **`breakpoint()` (Built-in từ Python 3.7)**: Thay vì gõ cả chục dòng `print()` để xem shape của Tensor lúc đang train bị sai ở đâu, bro chỉ cần chèn 1 chữ `breakpoint()` vào code. Khi chạy đến đó, chương trình sẽ tạm dừng, mở ra một màn hình terminal tương tác để bro gõ lệnh xem biến ngay tại thời điểm đó (tương đương với thư viện `pdb`). Khi test xong, gõ `c` (continue) để code chạy tiếp.

---

### 🎮 Bài Tập Thực Chiến: API Resilience

Làm AI Engineer là phải đối mặt với việc gọi API của OpenAI/Gemini thất bại liên tục (do mạng, do hết tiền, do server sập). Bro hãy thiết kế một cấu trúc xử lý lỗi cho tình huống này:

**Yêu cầu:**
Bro có một hàm giả lập gọi API như sau (cứ chạy là sẽ tự động văng lỗi):

```python
def call_llm_api(prompt):
    # Giả lập lỗi hết tiền (RateLimitError) hoặc lỗi mạng (ConnectionError)
    raise ValueError("API Key đã hết tiền!") 

```

**Nhiệm vụ của bro:**
Viết một đoạn code gọi hàm `call_llm_api("Xin chào")` nhưng phải áp dụng các luật sau:

1. Import module `logging` và cấu hình mức `INFO`.
2. Dùng block `try/except` để bẫy lỗi `ValueError` từ hàm trên.
3. Nếu dính lỗi, KHÔNG dùng `print`, mà dùng `logging.error(...)` để ghi nhận sự cố.
4. Dùng block `finally` để `logging.info(...)` dòng chữ: "Đóng luồng kết nối API." (để đảm bảo dù lỗi thì tài nguyên vẫn được giải phóng).
