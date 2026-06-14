import pandas as pd
import json
import os
import asyncio
def tien_xu_ly(url):
    data = pd.read_csv(url)
    print(f"Tổng số dòng ban đầu: {len(data)}")
    data.dropna(subset=['text'], inplace=True)
    data['text'] = data['text'].str.strip()
    data = data[data['text'] != ""]
    data.reset_index(drop=True, inplace=True)
    print(f"Tổng số dòng sau khi dọn rác: {len(data)}")
    print(data.head())
    data_list = data["text"].values.tolist()
    return data_list

def chunker(seq, size):
    """Chia danh sách lớn thành các lô nhỏ"""
    for i in range(0, len(seq), size):
        yield seq[i:i+size]
CHECKPOINT_FILE = "checkpoint.json"
def load_checkpoint() -> int:
    """Hàm này sẽ lưu lại tiến độ xử lý vào một file checkpoint.json"""
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE,'r') as f:
            data = json.load(f)
            return data.get("last_index", -1)
    return -1
def save_checkpoint(batch_index: int):
    with open(CHECKPOINT_FILE,'w') as f:
        json.dump({"last_index" : batch_index}, f)


async def mock_embedding_api(text: str):
    """Giả lập việc gửi 1 câu văn lên OpenAI và chờ vector trả về"""
    # TODO 1: Dùng lệnh ngủ bất đồng bộ để giả lập độ trễ mạng là 0.5 giây
    await asyncio.sleep(0.5)
    # Hàm này coi như thành công và trả về một dict mô phỏng
    return {"text": text, "status": "success"}


async def process_pipeline(data_list, batch_size=5):
    last_batch = load_checkpoint()
    print(f"Bắt đầu chạy từ lô số: {last_batch + 1}")

    # TODO 2: Gọi hàm chunker để ép data_list thành một list các lô (batches)
    batches = list(chunker(data_list, batch_size))


    # Chạy vòng lặp qua từng lô
    for batch_idx, batch in enumerate(batches):
        # TODO 3: Nếu batch_idx <= last_batch thì bỏ qua (continue) để không chạy lại lô cũ
        if batch_idx <= last_batch:
            continue
        print(f"Đang xử lý lô {batch_idx}...")
        try:
            # TODO 4: Tạo danh sách các task gọi mock_embedding_api cho từng câu text trong lô hiện tại (Dùng List Comprehension)
            tasks = [mock_embedding_api(text) for text in batch]

            # TODO 5: Dùng asyncio.gather để kích hoạt tất cả các task cùng lúc và lấy kết quả
            results = await asyncio.gather(*tasks)

            # TODO 6: Nếu gather thành công, gọi hàm save_checkpoint để chốt sổ lô hiện tại
            save_checkpoint(batch_idx)

            print(f" Xong lô {batch_idx}!")

        except Exception as e:
            print(f" Lỗi ở lô {batch_idx}: {e}")
            break  # Thoát vòng lặp để giữ an toàn dữ liệu
if __name__ == "__main__":
    url = r'/home/tung/AI_Engineer/PHASE 1 - Programming Foundation/PHASE_1_PROJECTS/PS3/customer_reviews.csv'
    data = tien_xu_ly(url)
    asyncio.run(process_pipeline(data, batch_size=3))
