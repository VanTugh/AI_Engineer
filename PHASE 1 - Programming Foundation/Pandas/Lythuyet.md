**1.9 Pandas (Essential for Data Work)**.

Nếu NumPy là bộ máy toán học lõi, thì **Pandas là lưỡi dao gọt dữ liệu** không thể thiếu trước khi đưa vào mô hình. Dữ liệu thực tế thường nằm ở file CSV, Excel, có cột tên, cột tuổi, và đầy rẫy dữ liệu bị thiếu (NaN). Pandas sinh ra để dọn dẹp đống lộn xộn này.

### 1. Khởi tạo & Khám phá dữ liệu (EDA)

* **Series (1D)**: Giống 1 cột trong Excel.
* **DataFrame (2D)**: Là toàn bộ bảng tính.
* **Bộ tứ siêu đẳng khi mới load data:**
* `df.head()`: Xem nhanh 5 dòng đầu xem mặt mũi data ra sao.
* `df.info()`: Cực quan trọng. Quét xem có bao nhiêu cột, kiểu dữ liệu từng cột là gì (có bị lẫn string vào cột số không), và có bao nhiêu giá trị bị thiếu.
* `df.describe()`: Thống kê nhanh Min, Max, Mean, Tứ phân vị của các cột số để xem data có bị lệch (outlier) không.
* `df.shape`: Số hàng, số cột.



### 2. Định vị (Indexing): `loc` vs `iloc`

* **`loc` (Location - Theo tên):** Tìm theo tên Cột hoặc tên Hàng (Index label).
* *Vd:* `df.loc[0:5, "Age"]` (Lấy cột Age từ dòng có tên là 0 đến tên là 5).


* **`iloc` (Integer Location - Theo vị trí):** Tìm theo tọa độ số (như ma trận NumPy).
* *Vd:* `df.iloc[0:5, 2]` (Lấy từ dòng 0 đến dòng 4, ở cột số 2).



### 3. Bộ lọc Boolean (Boolean filtering)

Cách nhanh nhất để trích xuất data thỏa mãn điều kiện.

* *Vd:* Lọc ra những người trên 18 tuổi: `adults = df[df['Age'] > 18]`
* Lọc nhiều điều kiện (dùng `&` cho AND, `|` cho OR): `df[(df['Age'] > 18) & (df['Gender'] == 'M')]`

### 4. Xử lý "Dữ liệu rác" (Missing values)

Train AI mà data có `NaN` (Not a Number) là hệ thống báo lỗi sập nguồn ngay.

* `isna()` / `isnull()`: Kiểm tra ô nào bị thiếu data (trả về True/False).
* `dropna()`: Xóa sổ luôn cả hàng nếu chứa dù chỉ 1 ô NaN (Cẩn thận, dễ mất data oan).
* **`fillna(value)` (Khuyên dùng):** Điền giá trị thay thế. Thường anh em sẽ điền bằng số trung bình của cột: `df['Age'].fillna(df['Age'].mean())`.

### 5. Gom nhóm & Tính toán (Aggregation)

Giống hệt `GROUP BY` trong SQL. Rất hay dùng để tạo đặc trưng mới (Feature Engineering).

* **`groupby('cột').agg(...)`:** Phân nhóm theo 1 cột và tính toán.
* *Vd:* Tính tuổi trung bình theo từng giới tính: `df.groupby('Gender')['Age'].mean()`


* **`value_counts()`:** Đếm tần suất. Tuyệt vời để kiểm tra Imbalanced Data (Dữ liệu mất cân bằng). VD: Đếm xem tập train có bao nhiêu ảnh chó, bao nhiêu ảnh mèo: `df['Label'].value_counts()`.

### 6. Gộp bảng (Combine DataFrames)

* **`concat([df1, df2])`:** Xếp chồng các bảng lên nhau (nối dọc hoặc ngang).
* **`merge(df1, df2, on='ID')`:** Nối bảng bằng một "chìa khóa" chung giống hệt SQL Join.

---

### 🎮 Bài Tập Thực Chiến: Data Preprocessing Pipeline

Hãy cài Pandas `pip install pandas` vào venv của bro, sau đó import `import pandas as pd` và giải quyết case study dọn data sau:

**Kịch bản:** Bro có một từ điển thông tin khách hàng (được giả lập thành DataFrame).

```python
import pandas as pd

data = {
    'CustomerID': [1, 2, 3, 4, 5],
    'Age': [25, 30, None, 45, 22],
    'Purchases': [3, 2, 5, 1, 4],
    'VIP': [False, True, False, True, False]
}
df = pd.DataFrame(data)

```

**Nhiệm vụ:**

1. **In ra số lượng ô bị thiếu (NaN)** trong toàn bộ DataFrame (Gợi ý: Kết hợp `isna()` và `sum()`).
2. **Xử lý thiếu hụt:** Cột `Age` đang có một người bị thiếu tuổi. Hãy lấp đầy ô trống này bằng tuổi trung bình (mean) của cột `Age`. (Lưu thẳng vào `df['Age']`).
3. **Lọc dữ liệu:** Trích xuất ra một DataFrame mới tên là `target_customers`, chỉ chứa những khách hàng **có trên 2 lượt mua hàng (Purchases > 2)**.
4. **Chốt sổ:** In cái bảng `target_customers` ra xem mặt mũi nó thế nào.
