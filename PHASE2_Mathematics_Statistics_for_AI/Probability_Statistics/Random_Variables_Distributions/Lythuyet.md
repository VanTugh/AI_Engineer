### 1. Biến ngẫu nhiên (Random Variables): Rời rạc vs Liên tục

Trong lập trình, biến là một hộp chứa giá trị (`x = 5`). Nhưng trong Xác suất, **Biến ngẫu nhiên ($X$)** là một hàm toán học ánh xạ một sự kiện thực tế thành một con số.

* **Discrete (Rời rạc):** Chỉ nhận các giá trị đếm được.
* *Ví dụ trong AI:* Phân loại ảnh. $X = 0$ (Chó), $X = 1$ (Mèo). Số lượng từ "Khuyến mãi" trong một email (0, 1, 2, 3... từ).


* **Continuous (Liên tục):** Nhận giá trị bất kỳ trong một khoảng.
* *Ví dụ trong AI:* Hệ thống tự lái đo khoảng cách tới xe phía trước ($12.45$ mét, $12.456$ mét...). Dự đoán giá nhà ($2.5$ tỷ).



### 2. PMF, PDF, CDF: Các tấm bản đồ xác suất

Làm sao để biết dữ liệu tập trung ở đâu? Chúng ta dùng các hàm phân phối.

* **PMF (Probability Mass Function):** Dành cho biến **rời rạc**. Trả lời câu hỏi: *"Xác suất để $X$ bằng chính xác $x$ là bao nhiêu?"*. (Ví dụ: Khả năng tung xúc xắc ra chính xác mặt 6 chấm là 1/6).
* **PDF (Probability Density Function):** Dành cho biến **liên tục**.

* *Cú lừa toán học:* Với biến liên tục, xác suất để nhiệt độ ngày mai bằng CHÍNH XÁC $25.000000^\circ C$ là bằng $0$. Do đó, PDF không cho ra xác suất tại 1 điểm, mà ta phải tính **diện tích dưới đường cong** trong một khoảng (ví dụ: xác suất nhiệt độ từ 24 đến 26 độ).
* **CDF (Cumulative Distribution Function):** Hàm phân bố tích lũy. Nó cộng dồn xác suất từ trái sang phải. Nó trả lời câu hỏi: *"Xác suất để $X \le x$ là bao nhiêu?"*. Đồ thị của nó luôn đi lên và chạm đỉnh ở mức 1 (tức 100%).

### 3. Expected Value, Variance, Standard Deviation

Khi bro cầm trong tay một Dataset chứa 1 tỷ dòng, bro không thể nhìn từng dòng được. Bro phải "nén" chúng lại thành các thông số cốt lõi này.

* **Expected Value / Mean ($\mu$ - Kỳ vọng):** Giá trị trung bình của dữ liệu. Nếu tung đồng xu (1 là ngửa, 0 là sấp) vô hạn lần, kỳ vọng là $0.5$. Trong AI, ta luôn muốn "Kỳ vọng của sai số" tiến về 0.
* **Variance ($\sigma^2$ - Phương sai):** Đo lường mức độ "nhiễu" (noise) hoặc độ phân tán của dữ liệu so với mức trung bình. Phương sai càng lớn, dữ liệu càng nhảy múa loạn xạ, AI càng khó học.
* **Standard Deviation ($\sigma$ - Độ lệch chuẩn):** Căn bậc hai của Phương sai. Vì phương sai bị bình phương lên (sai lệch đơn vị gốc), ta phải căn bậc 2 để đưa nó về cùng đơn vị với dữ liệu ban đầu cho dễ hiểu.

### 4. Covariance & Correlation (Hiệp phương sai & Tương quan)

Đây là công cụ để tìm ra "sợi dây liên kết" giữa 2 cột dữ liệu (Biến $X$ và Biến $Y$).

* **Covariance:** Đo lường hướng đi cùng nhau. Nếu $X$ tăng, $Y$ cũng tăng $\implies$ Covariance dương. Nếu $X$ tăng, $Y$ giảm $\implies$ Covariance âm. *Nhược điểm:* Giá trị của nó có thể chạy từ âm vô cực đến dương vô cực, không biết đâu mà lường.
* **Correlation ($r$ - Hệ số tương quan):** Vị cứu tinh! Nó lấy Covariance chia cho độ lệch chuẩn của cả 2 biến để "ép" giá trị về khoảng chuẩn từ **$-1$ đến $1$**.
* $r = 1$: Tương quan thuận tuyệt đối (Điểm Toán cao thì Lý chắc chắn cao).
* $r = -1$: Tương quan nghịch tuyệt đối.
* $r = 0$: Không có quan hệ gì (Như biểu đồ mây mù).
* *Bí quyết AI:* Nhớ lại bài Toán Ma trận (Matrix Rank) hôm trước không? Nếu 2 cột tính năng trong Dataset có Correlation xấp xỉ $1$, nghĩa là chúng chứa thông tin y hệt nhau. Ta có thể mạnh dạn **xóa bỏ 1 cột** để mô hình chạy nhanh hơn (Giảm chiều dữ liệu).



---

### 🎮 Bài Tập Thực Chiến: Khám Bệnh Cho Dữ Liệu

Sếp vừa gửi cho bro 2 mảng dữ liệu (đại diện cho thời gian học AI mỗi ngày, và điểm số bài test tương ứng của 5 sinh viên):

```python
import numpy as np

# Thời gian học (giờ)
hours_studied = np.array([1.0, 2.5, 3.0, 5.0, 7.5])

# Điểm số bài test (thang điểm 100)
test_scores = np.array([40, 55, 65, 80, 95])

```

**Nhiệm vụ của Intern:**
Sử dụng kho vũ khí của NumPy để tính toán nhanh các thông số thống kê sau:

1. Tính **Kỳ vọng (Mean)** của `hours_studied` và `test_scores`. (Dùng `np.mean`).
2. Tính **Độ lệch chuẩn (Standard Deviation)** của `test_scores`. (Dùng `np.std`). Xem điểm số của các bạn dao động bao nhiêu điểm so với mức trung bình.
3. Tìm **Hệ số tương quan (Correlation)** giữa số giờ học và điểm số. (Dùng `np.corrcoef(X, Y)` - lưu ý hàm này trả về một *ma trận*, bro hãy lấy giá trị ở vị trí `[0, 1]` nhé).
