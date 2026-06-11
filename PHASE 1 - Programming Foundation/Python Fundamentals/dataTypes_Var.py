val_1 = bool("False")
val_2 = bool("")
val_3 = int(3.99)
# Hỏi: val_1, val_2, val_3 lần lượt có giá trị là gì? Tại sao?
# True
# False
# 3
def process_temperature(temp):
    # API đôi khi trả về int (35), float (35.5), đôi khi lỗi nên trả về chuỗi ("35C")
    # Nhiệm vụ: Hãy viết 1 câu lệnh IF dùng isinstance() để kiểm tra.
    # Nếu temp là số (int hoặc float) thì in ra "OK", ngược lại in ra "Invalid data".
    if isinstance(temp, (int, float)):
        print("OK")
    else:
        print("Invalid data")
def normalize_data(data_list):
    data_list.append(100)
    return data_list


# Hỏi: In ra original_data lúc này sẽ là [1, 2, 3] hay [1, 2, 3, 100]? Tại sao?
if __name__ == '__main__':
    process_temperature("False")
    process_temperature("")
    process_temperature(3.99)
    original_data = [1, 2, 3]
    new_data = normalize_data(original_data)
    print(new_data)