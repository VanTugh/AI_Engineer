### 1. Lý Thuyết Trọng Tâm

#### 1.1. Các kiểu dữ liệu cơ bản (Basic Types)

Đây là những "nguyên liệu" cơ bản nhất để bro nhào nặn data:

* **`int` (Integer):** Số nguyên (vd: `10`, `-3`).
* **`float`:** Số thực, số thập phân (vd: `3.14`, `-0.001`).
* **`str` (String):** Chuỗi văn bản, luôn nằm trong ngoặc đơn hoặc kép (vd: `"AI Engineer"`, `'2026'`).
* **`bool` (Boolean):** Chỉ có 2 giá trị `True` hoặc `False`. Thường là kết quả của phép so sánh.
* **`None`:** Đại diện cho "không có gì cả" (tương tự `null` trong các ngôn ngữ khác). Rất hay dùng để khởi tạo một biến khi chưa có data từ API trả về.
#### 1.2. Ép kiểu (Type Conversion)
Trong pipeline AI, dữ liệu đọc từ file CSV hoặc API thường ở dạng `str`, phải ép nó về đúng kiểu số để model tính toán được.
* `int("10")` -> `10`
* `float("3.14")` -> `3.14`
* `str(100)` -> `"100"`
* **Đặc biệt với `bool()`:** Mọi giá trị rỗng hoặc bằng 0 (`0`, `""`, `[]`, `None`) khi ép sang `bool` đều là `False` (Falsy). Còn lại có data là `True` (Truthy).
#### 1.3. Kiểm tra kiểu: `type()` vs `isinstance()`
Khi viết code production, bro luôn phải validate data xem có đúng kiểu mình cần không trước khi đưa vào model.
* `type(x) == int`: Cách cơ bản nhất, nhưng **không khuyên dùng** trong code chuẩn.
* `isinstance(x, int)`: **Chuẩn production**. Nó không chỉ kiểm tra đúng kiểu đó, mà còn kiểm tra xem đối tượng có kế thừa từ kiểu đó không (rất quan trọng trong OOP).
#### 1.4. Mutable vs Immutable
Đây là khái niệm quan trọng nhất của bài này. Hiểu sai là data training bị xáo trộn lung tung.

* **Immutable (Bất biến):** Gồm `int`, `float`, `str`, `bool`, `tuple`.
* *Bản chất:* Khi bro gán giá trị mới, Python sẽ **tạo ra một ô nhớ hoàn toàn mới**. Giá trị cũ ở ô nhớ cũ không bị đụng tới.
* **Mutable (Có thể thay đổi):** Gồm `list`, `dict`, `set`.
* *Bản chất:* Khi bro thay đổi (thêm/xóa/sửa), Python thay đổi **trực tiếp trên ô nhớ gốc**.
* *Tại sao AI Engineer phải sợ nó?* Tưởng tượng bro có một `dataset = [1, 2, 3]`. Bro truyền nó vào hàm `clean_data(data)`. Hàm đó sửa `data`. Do `list` là Mutable, biến `dataset` gốc bên ngoài của bro cũng bị sửa theo! Model train xong sai bét mà không báo lỗi dòng nào.
### 1.5. String Manipulation: Vũ khí bí mật của AI Engineer
### 1. String Slicing: Cắt gọt dữ liệu (`s[start:stop:step]`)

Cú pháp này giúp bro trích xuất một phần của chuỗi cực nhanh. Nhớ quy tắc: **Bao gồm `start`, không bao gồm `stop**`.

* **Trích xuất:** `text = "Deep Learning"` -> `text[0:4]` trả về `"Deep"`.
* **Lấy từ cuối lên:** `text[-8:]` trả về `"Learning"` (rất hay dùng để lấy đuôi file, vd: `.csv`, `.png`).
* **Đảo ngược chuỗi (Trick phỏng vấn):** `text[::-1]` trả về `"gninraeL peeD"`.

### 2. String Methods: Bộ dụng cụ "làm sạch" Data

Khi làm việc với văn bản cào từ web (Crawl data) hoặc output từ LLM, data thường rất rác. Đây là các tool để dọn dẹp:

* **`strip()`:** Cạo sạch khoảng trắng (hoặc ký tự thừa) ở 2 đầu.
* *LLM hay trả về:* `"   \nKết quả là: 99%  "` -> `.strip()` -> `"Kết quả là: 99%"`.


* **`split(delimiter)` & `join(list)`:** Cặp bài trùng trong NLP.
* `split()`: Băm chuỗi thành List. Vd: `"AI,ML,Big Data".split(",")` -> `['AI', 'ML', 'Big Data']`. (Dùng để đếm số từ, tách token).
* `join()`: Gộp List thành chuỗi. Vd: `" ".join(['AI', 'ML'])` -> `"AI ML"`.


* **`replace(old, new)`:** Tìm và thay thế. Rất tốt để xóa các tag HTML nhiễu.
* **`find()`, `startswith()`, `endswith()`:** Dùng để check điều kiện.
* VD: Chặn luồng nếu output của model không bắt đầu bằng đúng format: `if not response.startswith("{""): return "Lỗi format JSON"`.



### 3. F-strings: Trái tim của Prompt Engineering (`f"..."`)

Từ Python 3.6 trở đi, f-string là cách format chuỗi bá đạo và nhanh nhất. Trong AI, chúng ta dùng nó liên tục để "bơm" dữ liệu động vào Prompt.

```python
user_input = "Làm sao để học PyTorch?"
confidence_score = 0.95678

# Bơm biến trực tiếp, đồng thời format số thập phân (.2f làm tròn 2 chữ số)
prompt = f"Người dùng hỏi: {user_input}. Độ tin cậy của câu trả lời phải đạt trên {confidence_score:.2f}"
# Kết quả: "Người dùng hỏi: Làm sao để học PyTorch?. Độ tin cậy của câu trả lời phải đạt trên 0.96"

```

### 4. Multiline strings: Khuôn đúc System Prompt (`"""..."""`)

Dùng 3 dấu ngoặc kép để viết chuỗi trên nhiều dòng. Đây là cú pháp tiêu chuẩn để viết Docstring (tài liệu cho hàm) hoặc viết System Prompt dài cho các model như GPT-4 hay Claude.

```python
system_prompt = """
Bạn là một AI Engineer tài năng năm 2026.
Nhiệm vụ của bạn là:
1. Đọc code Python.
2. Tìm ra bug.
3. Tối ưu hóa hiệu năng.
"""

```

---

### 🎮 Bài Tập Thực Chiến (Mini-Test)

Hãy tưởng tượng bro đang gọi API của một mô hình LLM để lấy thông tin. Mô hình đôi khi bị "ngáo" và trả về một chuỗi khá lộn xộn chứa các ký tự thừa và sai format.

Chuỗi trả về là:
`raw_output = "   \n\n THOUGHT: I should extract the entities. \nRESULT: apple, banana, cherry   ###   "`

**Nhiệm vụ của bro:** Bằng cách kết hợp `slicing` hoặc các `methods` ở trên, hãy viết một đoạn code ngắn (1-2 dòng) để xử lý `raw_output` sao cho kết quả cuối cùng thu được là một List chứa 3 loại quả:
`['apple', 'banana', 'cherry']`


### 1.6. Các kiểu dữ liệu phức tạp (Complex Data Structures)
### 1. Lists (Danh sách đa năng)

List là cấu trúc phổ biến nhất, dùng để chứa mọi thứ: từ danh sách đường dẫn ảnh đến lịch sử hội thoại của chatbot.

* **`append(item)` vs `extend(iterable)`:** * `append`: Nhét nguyên 1 cục vào cuối. VD: `[1, 2].append([3, 4])` -> `[1, 2, [3, 4]]`. (Hay dùng để gộp loss của từng epoch).
* `extend`: Mở nắp cục mới, lấy từng phần tử nhét vào cuối. VD: `[1, 2].extend([3, 4])` -> `[1, 2, 3, 4]`.


* **`pop(index)`:** Rút phần tử ra khỏi list (xóa đi và lấy giá trị đó).
* **`sort()` vs `reverse()`:** Sắp xếp data tại chỗ (in-place).

### 2. Tuples (Danh sách bất biến)

Giống List nhưng **Immutable** (không thể sửa sau khi tạo). Cú pháp dùng ngoặc tròn `()`.

* **Khi nào nên dùng Tuple thay vì List?** * Khi cần cố định kích thước/cấu trúc. Trong Deep Learning, hình dạng (shape) của dữ liệu luôn là tuple: `(batch_size, channels, height, width)`. Nếu dùng List, lỡ tay code sai làm thay đổi shape là model báo lỗi tanh bành ngay.
* Khi hàm return về nhiều giá trị: `return loss, accuracy` thực chất là đang trả về một tuple.



### 3. Dictionaries (Từ điển Key-Value)

Từ điển dùng ngoặc nhọn `{key: value}`. Đây là "vũ khí tối thượng" vì mọi API AI trả về JSON đều được Python parse thành Dictionary.

* **`.keys()`, `.values()`, `.items()`:** Trích xuất mảng chìa khóa, mảng giá trị, hoặc cả cặp (để chạy vòng lặp `for`).
* **Sự sống còn mang tên `.get(key, default)`:** * Nếu bro truy xuất `my_dict["score"]` mà API không trả về key "score", chương trình sẽ văng lỗi `KeyError` và sập luôn.
* Dùng `my_dict.get("score", 0.0)`: Nếu không có key "score", nó sẽ an toàn trả về mặc định là `0.0`. Không bao giờ sập app!



### 4. Sets (Tập hợp siêu tốc)

Set cũng dùng ngoặc nhọn `{1, 2, 3}` nhưng chỉ chứa các giá trị **duy nhất**.

* **Uniqueness:** Trong NLP, ném 1 triệu từ vào Set, bro sẽ ngay lập tức có được bộ từ vựng (vocabulary) không trùng lặp.
* **Toán tử siêu tốc:** Phép giao `&` (intersection), hợp `|` (union), trừ `-` (difference). Tốc độ tìm kiếm trong Set là tức thời, nhanh hơn List hàng nghìn lần với data lớn.

### 5. Nested Collections (Cấu trúc lồng ghép)

* **List of Dicts:** Dạng kinh điển của lịch sử chat (Conversation History) gửi cho OpenAI/Claude:
```python
messages = [
    {"role": "system", "content": "You are a helpful AI."},
    {"role": "user", "content": "Hello!"}
]

```



---

### 🎮 Bài Tập Thực Chiến (Mini-Test)

Vẫn như cũ nhé bro, thử sức với 2 bài toán thực tế dưới đây:

**Bài 1: Thao tác với "List of Dicts" (Mô phỏng LLM API)**
Giả sử bro đang quản lý mảng `messages` như ở trên.

```python
messages = [
    {"role": "system", "content": "You are a helpful AI."},
    {"role": "user", "content": "Hello!"}
]

# Nhiệm vụ 1: Làm sao để dùng method của List thêm một tin nhắn mới từ "assistant" với nội dung "Hi bro!" vào cuối mảng?
# Nhiệm vụ 2: In ra đúng chữ "Hello!" từ mảng messages bằng cách dùng Indexing và truy xuất Dictionary.

```

**Bài 2: Sức mạnh của Set trong xử lý NLP cơ bản**

```python
doc_1 = ["ai", "is", "the", "future"]
doc_2 = ["python", "is", "the", "key", "for", "ai"]

# Nhiệm vụ: Không dùng vòng lặp, hãy dùng Set để tìm ra những từ xuất hiện trong CẢ HAI tài liệu (doc_1 và doc_2).

```

### 1.6. Control Flow: Điều phối luồng xử lý (Routing) và AI Agents

### 1. `if / elif / else` (Hệ thống điều phối - Routing)

Đây là tư duy cốt lõi khi bro làm **Multi-LLM Orchestration** (Phase 7). Thay vì cứng nhắc dùng 1 model, hệ thống sẽ tự động chọn model dựa trên điều kiện:

* **Ví dụ:**
```python
if task_complexity == "hard":
    model = "gpt-4-turbo"
elif task_complexity == "medium":
    model = "claude-3-sonnet"
else:
    model = "haiku" # Tiết kiệm chi phí cho task dễ

```



### 2. Vòng lặp `for` & `while`

* **`for` loop (Lặp hữu hạn):** Quá quen thuộc rồi. Dùng để duyệt qua mảng data, duyệt qua các Epoch khi train model, hoặc gọi API cho một batch dữ liệu.
* **`while` loop (Lặp vô hạn/điều kiện) + `break/continue`:** Đây là "linh hồn" của **AI Agents** (như AutoGen hay LangGraph).
* *Bản chất Agent:* Một Agent hoạt động theo cơ chế `while True:` (Nghĩ -> Hành động -> Quan sát). Nó chỉ dừng lại (`break`) khi tìm được câu trả lời cuối cùng.
* *Retry API:* Khi gọi API bị lỗi quá tải (Rate Limit), bro dùng `while` để bắt hệ thống thử lại 3 lần. Nếu lỗi thì `continue` (bỏ qua bước hiện tại và thử lại), nếu thành công thì `break` thoát vòng lặp.



### 3. "Tam Thánh" vòng lặp Pythonic: `range()`, `enumerate()`, `zip()`

Trong Python, lặp theo kiểu `for i in range(len(list))` bị coi là "kém sang" (trừ khi dùng trong C/C++). Anh em viết code Python AI phải nắm trùm 3 hàm này:

* **`range(start, stop, step)`:** Tạo dãy số ảo. Tốn ít RAM. Dùng để đếm Epoch.
* **`enumerate(iterable)`:** Cứu tinh khi bro vừa cần lấy **giá trị** trong mảng, lại vừa cần biết **vị trí (index)** của nó.
```python
models = ["GPT", "Claude", "Gemini"]
for index, model in enumerate(models):
    print(f"Model thứ {index} là {model}")

```


* **`zip(list1, list2)`:** Hàm "kéo khóa". Dùng để ghép 2 hoặc nhiều list lại với nhau, duyệt song song cùng lúc. Trong Machine Learning, nó được dùng để so sánh nhãn thật (`y_true`) và nhãn dự đoán (`y_pred`).

---

### 🎮 Bài Tập Thực Chiến (Mini-Test)

Áp dụng luôn vào 2 bài toán cực kỳ sát thực tế khi làm việc với AI nhé bro:

**Bài 1: Cơ chế Retry API (Kết hợp `while`, `if`, `break`)**
Giả sử bro đang viết code để gọi API của OpenAI. API này rất hay báo lỗi mạng mạng.
Bro được giao nhiệm vụ viết một vòng lặp tối đa 3 lần thử (`max_retries = 3`):

* Mỗi lần lặp, in ra: `"Đang thử gọi API lần..."`.
* Giả sử lần thử thứ 2 API mới phản hồi thành công (gán một biến `success = True` ở lần 2).
* Nếu thành công, in ra `"Lấy data thành công!"` và thoát vòng lặp ngay lập tức.
* *(Gợi ý: Bro sẽ setup một biến đếm count và dùng vòng lặp while như thế nào?)*

**Bài 2: Đánh giá Model với `zip` và `enumerate**`
Bro có 2 mảng dữ liệu song song như sau:

```python
prompts = ["Tính 1+1", "Dịch chữ Cat", "Viết code web"]
results = ["2", "Mèo", "Lỗi Error"]

```

**Nhiệm vụ:** Chỉ dùng **MỘT** vòng lặp `for` duy nhất (kết hợp `zip` và `enumerate`), hãy in ra log theo đúng định dạng sau:

> "Task 0 - Prompt: Tính 1+1 | Kết quả: 2"
> "Task 1 - Prompt: Dịch chữ Cat | Kết quả: Mèo"
> "Task 2 - Prompt: Viết code web | Kết quả: Lỗi Error"

