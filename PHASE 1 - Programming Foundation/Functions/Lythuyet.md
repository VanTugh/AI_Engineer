### 1. Positional, Keyword & Default Arguments

Khi gọi một hàm, bro có thể truyền tham số theo vị trí (Positional) hoặc gọi đích danh tên (Keyword).

* **Default Arguments (Tham số mặc định):** Cực kỳ hữu dụng khi định nghĩa các siêu tham số (hyperparameters). Nếu người dùng không nhập, model sẽ tự dùng giá trị chuẩn.
```python
def train_model(data, epochs=10, learning_rate=0.001):
    # Nếu chỉ gọi train_model(my_data), hàm tự hiểu epochs=10 và lr=0.001
    pass

```


*Lưu ý xương máu:* **KHÔNG BAO GIỜ** dùng list hoặc dict làm default argument (vd: `def add_data(val, my_list=[])`). Nó sẽ gây lỗi nhớ chung ô nhớ (Mutable bug) mà chúng ta vừa bàn ở phần trước!

### 2. Trùm cuối AI SDKs: `*args` và `kwargs`

Đọc source code của PyTorch, Hugging Face hay LangChain, bro sẽ thấy chúng xuất hiện dày đặc. Chúng giúp hàm nhận số lượng tham số không giới hạn.

* **`*args` (Tuple):** Nhận vô số tham số theo vị trí.
* **`kwargs` (Dictionary):** Nhận vô số tham số theo dạng Keyword. Dùng để "tuồn" các tham số cấu hình linh hoạt xuống các layer bên dưới mà không cần định nghĩa trước.
```python
def call_llm(prompt, **kwargs):
    # kwargs lúc này là một Dictionary chứa các tham số phụ
    temperature = kwargs.get("temperature", 0.7)
    max_tokens = kwargs.get("max_tokens", 256)
    print(f"Calling LLM: Temp {temperature}, Tokens {max_tokens}")

call_llm("Hello", temperature=0.9, top_p=1.0) 

```



### 3. Return values & Tuple Unpacking

Các ngôn ngữ khác hàm thường chỉ trả về 1 giá trị. Python cho phép trả về nhiều giá trị dưới dạng Tuple và "bung" (unpack) chúng ra ngay lập tức.

```python
def evaluate_model():
    loss = 0.05
    accuracy = 0.98
    return loss, accuracy # Thực chất là trả về tuple (0.05, 0.98)

# Unpacking ngay khi gọi hàm
val_loss, val_acc = evaluate_model()

```

### 4. Lambda Functions & Recursion

* **Lambda (Hàm ẩn danh):** Hàm viết gọn trong 1 dòng, thường dùng làm tham số ném vào các hàm như `map()`, `filter()` hoặc `sort()`.
* *Ví dụ:* `sorted(list_dict, key=lambda x: x['score'])` (Sắp xếp danh sách kết quả AI trả về theo điểm số).


* **Recursion (Đệ quy):** Hàm tự gọi lại chính nó. Trong huấn luyện Deep Learning (như feedforward) thì ít dùng vì dễ gây tràn bộ nhớ (Stack Overflow). Nhưng lại cực kỳ hữu ích khi duyệt các cấu trúc cây phức tạp (như bóc tách file JSON nhiều tầng do API trả về).

### 5. Docstrings: Vũ khí của một Intern xuất sắc

Code chạy được là 1 chuyện, nhưng code để team đọc được lại là chuyện khác. Dùng chuỗi đa dòng `"""..."""` ngay dưới `def` để mô tả hàm. Các IDE như VS Code sẽ hiển thị nó khi người khác trỏ chuột vào hàm của bro.

---

### 🎮 Bài Tập Thực Chiến (Mini-Test)

Áp dụng các kỹ thuật trên để build 2 bộ hàm mô phỏng công việc AI nhé:

**Bài 1: Xây dựng Wrapper gọi API với `kwargs**`
Bro hãy viết một hàm tên là `generate_text(prompt, model_name="gpt-3.5", kwargs)`.

* Hàm này in ra màn hình `model_name` và `prompt`.
* Nếu người dùng có truyền thêm bất kỳ tham số phụ nào (như `temperature`, `max_tokens`), hãy duyệt qua cái `kwargs` đó (nhớ bài toán duyệt Dictionary bằng `.items()` ở phần trước không?) và in ra từng cặp `key: value`.

**Bài 2: Hàm tính toán và Tuple Unpacking**
Bro hãy viết hàm `compute_metrics(y_true, y_pred)` nhận vào 2 list.

* Giả sử bro chỉ cần đếm xem có bao nhiêu vị trí 2 list này giống nhau (số câu dự đoán đúng).
* Hàm phải `return` về 2 giá trị: `correct_count` (số lượng đúng) và `accuracy` (tỷ lệ % đúng).
* Sau đó gọi hàm và dùng Tuple Unpacking để gán vào 2 biến bên ngoài.

