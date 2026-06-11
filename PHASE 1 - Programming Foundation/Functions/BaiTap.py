def generate_text(prompt, model_name="gpt-3.5", **kwargs):
    """"Wrapper call API """
    print(f"prompt : {prompt} - model : {model_name}")
    if kwargs:
        print("tham so bo sung : ")
        for key, value in kwargs.items():
            print(f"{key}: {value}")


def compute_metrics(y_true, y_pred):
    """"Calculate accuracy matching true labels"""
    count = 0
    threshold = 0.5

    for pred, riel in zip(y_pred, y_true):
        # Bước 1: Ép xác suất về nhãn 0 hoặc 1 (dùng ternary operator cho gọn)
        pred_label = 1 if pred > threshold else 0

        # Bước 2: So sánh dự đoán với sự thật
        if pred_label == riel:
            count += 1

    # Có thể dùng len() luôn thay vì tạo biến total
    accuracy = count / len(y_pred)
    return count, accuracy

if __name__ == "__main__":
    generate_text(
        "Hãy viết một bài thơ về mùa xuân",
        model_name="gpt-4",
        temperature=0.8,
        max_tokens=100
    )
    y_pred = [0.2, 0.1, 0.6, 0.78 , 0.12, 0.9]
    y_true = [1, 0, 1, 1, 0, 1, 1]
    count, accuracy = compute_metrics(y_true, y_pred)
    print(f"so luong du doan dung : {count} - do chinh xac : {accuracy:.2f}")
