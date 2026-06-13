import pandas as pd
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
    yield 
if __name__ == "__main__":
    url = r'/home/tung/AI_Engineer/PHASE 1 - Programming Foundation/PHASE_1_PROJECTS/PS3/customer_reviews.csv'
    data = tien_xu_ly(url)