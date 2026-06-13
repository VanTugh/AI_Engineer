**1.11 Python for AI Workflows (Quy trình làm việc thực tế của AI)**.

Đây là những công cụ "nhỏ nhưng có võ" mà bro sẽ dùng hàng ngày khi làm Machine Learning và Deep Learning. Thiếu chúng, luồng làm việc sẽ cực kỳ tù túng.

### 1. Jupyter Notebooks & Google Colab (Môi trường nghiên cứu)

* Khi làm AI, chúng ta không code một lèo rồi mới chạy, mà phải chạy thử từng dòng, xem từng cái biểu đồ (EDA). **Jupyter** chia code thành các cell (ô) để chạy độc lập.
* **Colab** là chân ái của sinh viên AI vì nó cho mượn GPU (T4, A100) miễn phí.
* **Magic commands:** Bắt đầu bằng `%`. Ví dụ `%timeit` để đo tốc độ của 1 cell, hoặc `!pip install` để chạy lệnh terminal ngay trong notebook.

### 2. `tqdm` (Thanh tiến trình chống trầm cảm)

Khi train một mô hình Deep Learning qua 10.000 batches, nếu không có gì báo hiệu, màn hình console sẽ đen ngòm, bro sẽ không biết máy đang chạy hay bị treo.

* Chỉ cần bọc một vòng lặp bất kỳ vào `tqdm`, nó sẽ hiển thị một thanh tiến trình chạy % cực xịn xò kèm thời gian ước tính (ETA).
* *Cú pháp:* `for idx in tqdm(range(100)):`

### 3. `argparse` (Truyền lệnh từ Terminal)

Khi mang code lên server Ubuntu để chạy, bro không thể mở file code ra sửa tham số được. Phải dùng `argparse` để truyền tham số từ bên ngoài.

* *Cách chạy:* `python train.py --epochs 50 --batch_size 32`

### 4. `dotenv` (Bảo mật API Key - TỬ HUYỆT CỦA AI ENGINEER)

Khi gọi API của OpenAI, Claude hay Gemini, bro sẽ có một đoạn mã bí mật (API Key). **TUYỆT ĐỐI KHÔNG BAO GIỜ** gõ thẳng chuỗi Key này vào file code `.py`. Nếu bro lỡ tay `git push` lên Github, bot của các hacker sẽ quét được trong 3 giây và dùng key của bro để đào coin, bill có thể lên tới hàng nghìn đô.

* **Cách làm chuẩn:** Tạo một file tên là `.env` chứa `OPENAI_API_KEY=sk-...`. Trong code Python, dùng thư viện `python-dotenv` để load nó vào làm biến môi trường.

### 5. Seeding for reproducibility (Cố định sự ngẫu nhiên)

AI chứa đầy sự ngẫu nhiên (khởi tạo trọng số, trộn data, chia batch). Nếu mỗi lần chạy ra một kết quả khác nhau thì bro không thể debug xem model tốt lên là do code chuẩn hay do... ăn may.

* Trước khi train, LUÔN LUÔN phải khóa random lại (Seeding) bằng 3 dòng chú thuật này:

```python
random.seed(42)
np.random.seed(42)
torch.manual_seed(42)

```

### 6. Saving/loading models (Lưu trữ và phục hồi)

Train xong model mất 3 ngày, tắt máy đi là mất hết nếu không lưu lại trọng số (weights).

* **`pickle`**: Lưu các object Python cơ bản.
* **`joblib`**: Chuyên dùng cho các model của Scikit-learn (như Random Forest, SVM) vì nó nén các ma trận numpy khổng lồ cực tốt.
* **`torch.save()`**: Tiêu chuẩn vàng để lưu mạng nơ-ron của PyTorch thành các file `.pth` hoặc `.pt`.

---

### 🎮 Bài Tập Thực Chiến: Setup Workflow Tiêu Chuẩn

Để mô phỏng đúng môi trường đi thực tập, bro hãy viết một script Python kết hợp 2 kỹ năng sống còn nhất: **Bảo mật biến môi trường (`dotenv`)** và **Hiển thị tiến trình (`tqdm`)**.

*(Lưu ý: Môi trường `venv` của bro cần cài thư viện trước: `pip install python-dotenv tqdm`)*

**Nhiệm vụ:**

1. Hãy giả lập (tưởng tượng) bro đã tạo một file `.env` cùng thư mục chứa dòng chữ: `SECRET_TOKEN=xyz_123_abc`.
2. Trong file Python, import `os` và hàm `load_dotenv` từ module `dotenv`. Hãy gọi hàm `load_dotenv()` để nạp biến.
3. Dùng `os.getenv("SECRET_TOKEN")` để lấy cái key đó ra và `print` thử xem có lấy thành công không.
4. Import `tqdm` và thư viện `time`. Viết một vòng lặp `for` chạy 10 lần, được bọc bởi thanh tiến trình `tqdm`. Trong mỗi lần lặp, cho chương trình ngủ 0.2 giây (`time.sleep(0.2)`) để bro ngắm được thanh tiến trình chạy mượt mà trên terminal.
