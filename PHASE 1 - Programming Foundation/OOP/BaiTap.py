class TextDataset:
    # 1. Khai báo một Class variable có tên là "task" với giá trị "NLP"
    task = "NLP"
    def __init__(self, texts, labels):
        # 2. Khởi tạo 2 Instance variables để lưu trữ texts và labels
        self.texts = texts
        self.labels = labels

    def __len__(self):
        # 3. Trả về tổng số lượng dữ liệu có trong texts
        return len(self.texts)

    def __getitem__(self, idx):
        # 4. Trả về một dictionary chứa 1 câu và nhãn tương ứng ở vị trí idx
        # Ví dụ: {"text": "AI is great", "label": 1}
        return {"text": self.texts[idx], "label": self.labels[idx]}

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