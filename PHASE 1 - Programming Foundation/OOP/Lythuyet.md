### 1. Lõi của OOP: Classes, Instances, `__init__` & `self`

* **Class** là bản thiết kế (blueprint). **Instance** là một thực thể cụ thể được tạo ra.
* **`__init__`**: Hàm khởi tạo. Chạy ngay lập tức khi instance được sinh ra để thiết lập cấu hình ban đầu (như architecture, weights).
* **`self`**: Đại diện cho chính cái instance đó. Dùng `self.x` để lưu dữ liệu sống sót xuyên suốt vòng đời của object.

### 2. Class vs Instance variables

* **Instance variables** (biến dùng `self.`): Thuộc về riêng từng object. Ví dụ: learning rate của model A có thể khác model B.
* **Class variables** (biến khai báo ngay dưới tên class, không có `self.`): Dùng chung cho TẤT CẢ các object. Ví dụ: định nghĩa `device = "cuda"` mặc định cho mọi model thuộc class đó.

### 3. Kế thừa (Inheritance), `super()` & Overriding

Tuyệt chiêu để bro tạo ra các mạng AI custom mà không phải code lại từ đầu.

* **Kế thừa & `super()`:** Bro tạo một class con kế thừa class cha (ví dụ `nn.Module` trong PyTorch). Bro BẮT BUỘC phải gọi `super().__init__()` để class cha setup các thành phần lõi trước, sau đó bro mới thêm các layer của riêng mình.
* **Overriding:** Viết đè lại hàm của class cha. Kinh điển nhất là việc viết đè hàm `forward()` để định nghĩa luồng dữ liệu đi qua mạng nơ-ron như thế nào.

### 4. Magic Methods: `__repr__`, `__str__`, `__len__`, `__getitem__`

Những hàm có 2 dấu gạch dưới (dunder) giúp object tương tác mượt mà với Python gốc.

* **`__repr__` / `__str__**`: Khi bro `print(model)`, nó in ra cấu trúc các layer đẹp mắt thay vì một dải địa chỉ bộ nhớ khó hiểu là nhờ 2 hàm này.
* **`__len__` & `__getitem__` (Bí kíp Custom Dataset)**: Khi huấn luyện AI với Big Data, không ai load cả chục GB ảnh vào RAM. Bro phải viết một class `CustomDataset`, định nghĩa `__len__` để model biết tổng số data, và `__getitem__(self, idx)` để model tự động bốc đúng 1 batch data ở vị trí `idx` đưa vào train.

### 5. Bộ 3 quyền lực: `@property`, `@staticmethod`, `@classmethod`

* **`@property`**: Biến một method thành một thuộc tính (attribute). Dùng để bảo vệ an toàn cho các siêu tham số (hyperparameters), chỉ cho phép đọc chứ không cho phép sửa bậy bạ từ bên ngoài.
* **`@staticmethod`**: Hàm tiện ích nhét vào trong class cho gọn, không cần dùng `self`. (VD: Hàm tính toán độ đo F1-score không phụ thuộc vào trạng thái của model).
* **`@classmethod` (Đỉnh cao của AI Framework)**: Không dùng `self` mà dùng `cls`. Chắc bro đã quen với câu lệnh `Model.from_pretrained("path")` trong Hugging Face? Đó chính là classmethod! Nó cho phép khởi tạo model theo một cách khác biệt (từ file weights) thay vì dùng `__init__` mặc định.

### 6. Abstract classes (ABC)

Lớp trừu tượng định nghĩa "luật chơi".
Khi xây dựng Agentic Workflow bằng LangChain, framework sẽ cấp cho bro một class cơ sở `BaseLLM`. Class này dùng thư viện `abc` để ép buộc: *"Nếu anh muốn viết wrapper cho mô hình AI của riêng anh, anh bắt buộc phải override hàm `_generate()`. Nếu không, tôi báo lỗi ngay lúc biên dịch!"*.

---

### 🎮 Bài Tập Thực Chiến: Xây dựng Custom Dataset

Để thực sự ngấm phần này, chúng ta hãy viết một khung Custom Dataset thu nhỏ (rất hay gặp khi xử lý dữ liệu để fine-tune).

**Nhiệm vụ của bro:**
Hãy hoàn thiện đoạn code sau. Đọc kỹ các `# TODO` để ráp đúng cú pháp OOP vào nhé.

```python
class TextDataset:
    # 1. Khai báo một Class variable có tên là "task" với giá trị "NLP"
    
    def __init__(self, texts, labels):
        # 2. Khởi tạo 2 Instance variables để lưu trữ texts và labels
        pass

    def __len__(self):
        # 3. Trả về tổng số lượng dữ liệu có trong texts
        pass

    def __getitem__(self, idx):
        # 4. Trả về một dictionary chứa 1 câu và nhãn tương ứng ở vị trí idx
        # Ví dụ: {"text": "AI is great", "label": 1}
        pass

    @classmethod
    def from_csv(cls, file_path):
        # 5. Giả lập việc đọc file CSV (ở đây ta fix cứng dữ liệu cho nhanh).
        # Hãy dùng cls() để khởi tạo và trả về object TextDataset với dữ liệu giả lập dưới đây:
        fake_texts = ["Hello AI", "Learn Python"]
        fake_labels = [0, 1]
        pass

# --- TEST CODE ---
# Khởi tạo dataset từ file csv (thông qua classmethod)
my_dataset = TextDataset.from_csv("dummy_path.csv")

# Kiểm tra chiều dài (sẽ tự động gọi __len__)
print(f"Tổng số mẫu: {len(my_dataset)}")

# Lấy phần tử đầu tiên (sẽ tự động gọi __getitem__)
print(f"Data số 0: {my_dataset[0]}")

```
