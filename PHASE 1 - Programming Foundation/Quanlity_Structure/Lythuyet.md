**1.10 Code Quality & Project Structure (Chất lượng code & Cấu trúc dự án)**.
Phần này chính là lằn ranh phân biệt giữa "code chạy cho biết" và "code chuẩn production". Khi bro tham gia các dự án AI lớn hoặc đi thực tập, không ai ném toàn bộ 10.000 dòng code vào một file `main.py` cả. Mọi thứ phải được tổ chức khoa học.
Dưới đây là bộ tiêu chuẩn bắt buộc:
### 1. Quản lý Môi trường & Dependencies
* **Virtual environments (`venv` / `conda`)**: Cái này anh em mình đã chốt và setup xong xuôi ở mấy tin nhắn trước rồi. Nguyên tắc vàng: Mỗi project 1 môi trường.
* **`requirements.txt` & `pip freeze**`:
* Khi code xong, bro phải đóng gói danh sách các thư viện đã dùng để máy khác cũng chạy được.
* Lệnh: `pip freeze > requirements.txt` (Xuất danh sách thư viện ra file).
* Khi mang sang máy khác/server mới: `pip install -r requirements.txt`.



### 2. Cấu trúc Module & `__init__.py`

* Đừng dồn hết code vào 1 file. Hãy chia nhỏ: `data_loader.py`, `model.py`, `train.py`.
* **`__init__.py`**: Khi bro tạo một thư mục (vd: `my_model/`), bro phải thả một file rỗng tên là `__init__.py` vào đó. File này báo cho Python biết: *"Đây không phải thư mục bình thường, đây là một Package, cho phép import các file bên trong nó!"*.

### 3. Type Hints (Gợi ý kiểu dữ liệu)

Python là ngôn ngữ *dynamic typing* (không ép kiểu), nhưng trong code production, không có Type Hints thì lúc đọc code sẽ mù tịt không biết biến đó là `int` hay `list`.

* **Cú pháp:** `def process_data(data: list, is_train: bool = True) -> str:`
* Tác dụng: Giúp IDE (như VSCode) tự động gợi ý code (autocomplete) cực mạnh và phát hiện lỗi sai kiểu ngay lúc đang gõ.

### 4. Dataclasses - Siêu cấu trúc lưu cấu hình

Khi bro có 20 siêu tham số (hyperparameters) cho một mô hình, việc dùng Dictionary rất dễ gõ sai chính tả (KeyError). Việc tạo Class bình thường thì phải viết hàm `__init__` dài dòng.

* **`@dataclass`** (từ Python 3.7) là chân ái. Nó tự động sinh ra `__init__` và `__repr__` cho bro.

```python
from dataclasses import dataclass

@dataclass
class ModelConfig:
    learning_rate: float
    batch_size: int = 32
    optimizer: str = "Adam"

# Sử dụng cực gọn:
config = ModelConfig(learning_rate=0.001)
print(config.batch_size) # In ra 32

```

### 5. Kiểm thử (Unit tests với `pytest`)

Code AI thường dính "bug im lặng" (code vẫn chạy nhưng toán học bị sai). Phải viết test.

* `pytest` là framework mạnh nhất hiện nay.
* Chỉ cần viết các hàm bắt đầu bằng chữ `test_`, ví dụ `test_data_loader()`, sau đó gõ lệnh `pytest` trên terminal, nó sẽ tự quét và chạy kiểm tra.

### 6. Linting & Formatting (`ruff`, `flake8`, `black`)

Đây là cảnh sát giao thông của code.

* **`black`**: Formatter không khoan nhượng. Gõ lệnh `black code_cua_ban.py`, nó tự động format lại khoảng trắng, thụt lề, dấu phẩy chuẩn 100% style PEP8.
* **`ruff`** (hoặc `flake8`): Linter tốc độ ánh sáng. Quét code để phát hiện các lỗi như: biến được khai báo nhưng chưa sử dụng, import thừa thư viện, v.v.

---

### 🎮 Bài Tập Thực Chiến: Clean Code Config

Để "ngấm" chuẩn production, bro hãy kết hợp **Type Hints** và **Dataclasses** để viết một đoạn script nhỏ nhé.

**Nhiệm vụ:**

1. Import `dataclass` từ thư viện `dataclasses`.
2. Tạo một dataclass tên là `LLMConfig`. Bên trong chứa 3 thông số có sử dụng Type Hints:
* `model_name` (chuỗi văn bản)
* `temperature` (số thực, mặc định là 0.7)
* `max_tokens` (số nguyên, mặc định là 512)


3. Viết một hàm tên là `initialize_llm()`.
* Hàm này nhận vào một tham số `config` có kiểu dữ liệu là `LLMConfig`.
* Hàm này cam kết trả về kiểu `bool` (chỉ định bằng `-> bool:`).
* Nội dung hàm: Chỉ cần `print` ra cái `config` đó và `return True`.


4. Viết phần thực thi (`if __name__ == "__main__":`), khởi tạo một cái config với `model_name="gpt-4"`, truyền vào hàm `initialize_llm` và in kết quả `True/False` ra màn hình.
