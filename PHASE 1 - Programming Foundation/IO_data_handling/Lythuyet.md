### 1. `open()` và Context Managers (`with`)

Nguyên tắc số 1 khi thao tác file: **Mở ra thì phải đóng lại**. Nếu quên đóng file, hệ thống sẽ bị tràn RAM (memory leak).

* **Context Manager (`with`)** là vị cứu tinh. Nó sẽ tự động đóng file ngay khi code chạy xong khối lệnh, cho dù có bị lỗi giữa chừng.

```python
# Chuẩn production
with open("dataset.txt", "r", encoding="utf-8") as file:
    data = file.read()
# Ra khỏi lề 'with', file tự động được đóng lại.

```

### 2. Xử lý CSV và JSON

* **CSV module:** Dùng để đọc các bảng dữ liệu cơ bản. (Tuy nhiên, trong thực tế làm Machine Learning, anh em mình sẽ thường dùng thư viện Pandas ở mục 1.9 để đọc CSV cho mạnh mẽ và tối ưu hơn).
* **JSON (`json.load()`, `json.dump()`):** Đây là định dạng "vua" khi giao tiếp với API của các LLM (OpenAI, Gemini).
* `json.dump(data, file)`: Lưu dictionary của Python thành file `.json`. Hay dùng để lưu file config siêu tham số (hyperparameters) của mô hình.
* `json.load(file)`: Đọc file `.json` biến ngược lại thành dictionary.



### 3. Pickle: "Tủ đông" của Python

Khi bro tiền xử lý xong một ma trận dữ liệu khổng lồ, hoặc train xong một model scikit-learn, bro muốn "đóng băng" nó lại để lần sau dùng luôn mà không phải tính lại.

* `pickle.dump(model, file)`: Lưu object Python dưới dạng byte nhị phân.
* `pickle.load(file)`: Đọc file byte lên lại thành object.
* **⚠️ Cảnh báo bảo mật:** Chỉ unpickle những file do chính tay bro tạo ra. Mã độc thường được giấu trong các file `.pkl` trôi nổi trên mạng (hacker hay thả mã độc vào các file model giả mạo). Hugging Face hiện nay đang chuyển sang dùng định dạng an toàn hơn là `.safetensors`.

### 4. Quản lý đường dẫn: `os` vs `pathlib`

Khi code chạy trên máy bro (Windows) thì đường dẫn dùng `\`, nhưng quăng lên server Ubuntu để train model thì nó lại dùng `/`. Nếu hardcode đường dẫn bằng chuỗi (string) thì code sẽ sập ngay.

* **`os.path.join("data", "images", "cat.jpg")`:** Cách cổ điển. Tự động thêm đúng dấu gạch chéo theo hệ điều hành.
* **`pathlib.Path`:** Cách hiện đại (Python 3.4+). Nó biến đường dẫn thành một Object cực kỳ xịn xò.

```python
from pathlib import Path
# Nối chuỗi bằng toán tử / cực kỳ Pythonic
data_dir = Path("dataset") / "images" 
data_dir.mkdir(parents=True, exist_ok=True) # Tự tạo thư mục nếu chưa có

```

### 5. `glob`: Trùm gom nhóm file (Batch Processing)

Khi bro có 1 thư mục chứa 10.000 ảnh để train mô hình phân loại, bro không thể gõ tay từng tên file được.

* `glob` giúp lọc file theo pattern.

```python
import glob
# Lấy toàn bộ đường dẫn của các file .png trong thư mục train_data
image_paths = glob.glob("train_data/*.png")

```

---

### 🎮 Bài Tập Thực Chiến: Data Pipeline Mini

Hãy tưởng tượng bro đang viết một script chuẩn bị dữ liệu. Bro có một danh sách các kết quả đánh giá mô hình (Dictionary) và cần lưu nó xuống ổ cứng một cách chuyên nghiệp.

**Yêu cầu:**

1. Khai báo một dictionary `config = {"model": "ResNet", "epochs": 50, "batch_size": 32}`.
2. Dùng `pathlib.Path` để tạo một thư mục tên là `checkpoints` (nếu thư mục đã tồn tại thì không báo lỗi).
3. Dùng Context Manager (`with open...`) và module `json` để lưu cái `config` kia vào một file tên là `model_cfg.json` nằm bên trong thư mục `checkpoints` vừa tạo.

