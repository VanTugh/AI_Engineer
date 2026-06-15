### 1. Gia tộc "Công bằng tuyệt đối" & "Quả chuông thần thánh"

Hai phân phối này là xương sống của mọi thuật toán Machine Learning.

* **Uniform (Phân phối Đều):** * *Bản chất:* Mọi kết quả đều có xác suất xảy ra y hệt nhau (như mặt phẳng nằm ngang).
* *AI Context:* Khi bro khởi tạo Mạng Nơ-ron, ta không bao giờ set tất cả trọng số (weights) bằng $0$, mà thường dùng `np.random.uniform()` để gán cho chúng các giá trị ngẫu nhiên công bằng từ $-1$ đến $1$ nhằm phá vỡ sự đối xứng.


* **Gaussian / Normal (Phân phối Chuẩn):**

* *Bản chất:* Ông vua của ngành thống kê. Đồ thị hình quả chuông hoàn hảo. Nó được quy định bởi 2 tham số: Kỳ vọng ($\mu$) nằm ở đỉnh chuông, và Độ lệch chuẩn ($\sigma$) quyết định chuông phình to hay hẹp.
* *Định lý Giới hạn Trung tâm (Central Limit Theorem):* Bất cứ thứ gì trong tự nhiên bị tác động bởi nhiều yếu tố ngẫu nhiên độc lập (chiều cao con người, sai số đo lường máy móc) thì cuối cùng đều hội tụ về Phân phối Chuẩn.
* *AI Context:* Khi chuẩn hóa dữ liệu (Standardization), ta ép dữ liệu gốc về dạng chuẩn với $\mu = 0$ và $\sigma = 1$ để AI học nhanh hơn.

### 2. Gia tộc "Đúng/Sai" (Discrete)

Dùng cho các bài toán phân loại (Classification).

* **Bernoulli:** * *Bản chất:* Chỉ có **1 lần thử duy nhất**. Kết quả là Thành công (xác suất $p$) hoặc Thất bại (xác suất $1-p$). Như tung một đồng xu.
* *AI Context:* Đầu ra của hàm Sigmoid trong phân loại nhị phân chính là xác suất $p$ của phân phối Bernoulli (ví dụ: $p = 0.8$ là Chó, vậy $0.2$ là Mèo).


* **Binomial (Phân phối Nhị thức):**
* *Bản chất:* Chính là Bernoulli nhưng lặp lại **$N$ lần độc lập**. Trả lời câu hỏi: *"Tung đồng xu $N$ lần, xác suất ra đúng $k$ mặt ngửa là bao nhiêu?"*.



### 3. Gia tộc "Thời gian & Không gian"

Rất hay dùng trong phân tích dữ liệu chuỗi thời gian (Time-series) hoặc vận hành hệ thống Server MLOps.

* **Poisson:** * *Bản chất:* Đo lường **SỐ LƯỢNG biến cố** xảy ra trong một khoảng thời gian cố định.
* *Ví dụ:* Số lượng request gửi đến server API của ChatGPT trong 1 giây, hoặc số vụ tai nạn giao thông trong 1 ngày.


* **Exponential (Phân phối Mũ):**
* *Bản chất:* Trái ngược với Poisson. Nó đo lường **THỜI GIAN CHỜ** giữa 2 biến cố liên tiếp.
* *Ví dụ:* Thời gian server AI sẽ chạy ổn định trước khi bị sập (Time until failure).



### 4. Gia tộc "Đa chiều" - Linh hồn của NLP

* **Multinomial (Phân phối Đa thức):**
* *Bản chất:* Là bản nâng cấp của Binomial. Thay vì tung đồng xu (2 mặt), ta tung một con xúc xắc có $K$ mặt, lặp lại $N$ lần.
* *AI Context:* Trong Xử lý ngôn ngữ tự nhiên (NLP), một cuốn từ điển có $K$ từ (ví dụ 50,000 từ). Một câu văn dài $N$ từ chính là một phép thử Multinomial. Thuật toán Naive Bayes ở bài trước bản chất là sử dụng phân phối này để đếm tần suất xuất hiện của các từ ("Bag of Words") và dự đoán nhãn!

---

### 5. Gia tộc "Hỗn hợp" - Khi thế giới không hoàn hảo
* **Mixture Models (Mô hình Hỗn hợp):**
* *Bản chất:* Thế giới thực thường không tuân theo một phân phối duy nhất. Mô hình hỗn hợp cho phép chúng ta kết hợp nhiều phân phối khác nhau để mô tả dữ liệu phức tạp hơn.
  * *Ví dụ:* Dữ liệu chiều cao của khuôn mặt con người có thể được mô hình hóa bằng một hỗn hợp của nhiều phân phối Gaussian, mỗi phân phối đại diện cho một nhóm tuổi hoặc giới tính khác nhau.
  * *AI Context:* Trong Machine Learning, Mixture Models thường được sử dụng trong các thuật toán phân cụm (Clustering) như Gaussian Mixture Models (GMM) để phát hiện các nhóm tiềm ẩn trong dữ liệu mà không cần nhãn.
  * * *Ứng dụng:* Mixture Models cũng rất hữu ích trong việc xử lý dữ liệu bị nhiễu hoặc có nhiều nguồn gốc khác nhau, giúp cải thiện hiệu suất của các mô hình dự đoán và phân loại.
  * * *Lưu ý:* Việc xác định số lượng phân phối con trong một Mixture Model có thể là một thách thức và thường yêu cầu các phương pháp như Bayesian Information Criterion (BIC) hoặc Cross-Validation để lựa chọn mô hình tốt nhất.
  * * * *Tóm lại:* Mixture Models là một công cụ mạnh mẽ để mô hình hóa dữ liệu phức tạp và đa dạng, giúp AI hiểu rõ hơn về thế giới thực và cải thiện khả năng dự đoán của các mô hình học máy.
  
Sự thật là: Học Xác suất Thống kê ở trường đại học đa số là giải tích phân bằng tay, cực kỳ buồn ngủ và hàn lâm. Nhưng học Xác suất Thống kê dưới góc độ của một AI Engineer thì lại cực kỳ thực dụng, vì ta dùng **Code** để nhìn thấy toán học chạy trước mắt mình!

Tôi sẽ thiết kế lại toàn bộ phần **Biến ngẫu nhiên & Phân phối** này theo "hệ Code", đi chậm lại và đảm bảo mọi công thức LaTeX đều render chuẩn xác trên file `.md` của bro.

Chúng ta sẽ chỉ tập trung vào 2 gia tộc mạnh nhất: **Normal (Liên tục)** và **Binomial (Rời rạc)**.

---

### 1. Bản chất của "Phân phối" (Distribution) là gì?

Hãy tưởng tượng bro có một cái hộp chứa 100 con xúc xắc. Bro tung tất cả chúng lên.

* Trục ngang ($x$): Là giá trị kết quả (Từ 1 đến 6 chấm).
* Trục dọc ($y$): Là số lượng xúc xắc rơi vào kết quả đó (hoặc Xác suất phần trăm).
* **Đường vẽ nối các đỉnh của các cột đó lại** $\rightarrow$ Chính là đường **Phân phối (Distribution)**.

Nó đơn giản là một "Bản đồ" cho AI biết: *"Ở thế giới này, con số nào dễ xuất hiện nhất, con số nào là trường hợp hiếm (Outlier)?"*

---

### 2. Phân phối Chuẩn (Normal / Gaussian Distribution) - Vua của AI

Đây là phân phối dành cho **Biến liên tục** (chiều cao, cân nặng, giá nhà, sai số của AI).

**Tại sao nó lại hình quả chuông?**
Bởi vì Định lý Giới hạn Trung tâm (Central Limit Theorem) đã chứng minh: Bất cứ thứ gì trong tự nhiên bị tác động bởi hàng ngàn yếu tố ngẫu nhiên nhỏ bé cộng gộp lại, thì kết quả cuối cùng LUÔN LUÔN tạo ra hình quả chuông.

* Ví dụ: Chiều cao của bro bị tác động bởi gen bố, gen mẹ, lượng sữa uống lúc nhỏ, tư thế ngồi... Nếu lấy chiều cao của 1 triệu người Việt Nam vẽ lên đồ thị, nó chắc chắn ra hình quả chuông hoàn hảo.

**Công thức PDF (Hàm mật độ xác suất):**
Hàm số tạo ra cái đường cong quả chuông đó trông rất đáng sợ, nhưng bro chỉ cần để ý 2 tham số lõi:


$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^2}$$

* $\mu$ (Kỳ vọng / Mean): Là đỉnh của quả chuông. Quyết định quả chuông nằm ở đâu trên trục $x$.
* $\sigma$ (Độ lệch chuẩn / Standard Deviation): Quyết định quả chuông **béo lùn** hay **thon cao**.

Để bro thực sự "cảm giác" được hai ký hiệu $\mu$ và $\sigma$ này uốn nắn dữ liệu như thế nào, hãy tương tác với Widget mô phỏng toán học dưới đây:

**Quy tắc vàng 68-95-99.7 (Cực kỳ quan trọng khi làm Data):**
Nhìn vào vùng được tô màu trong Widget, bro sẽ thấy quy luật bất biến của Mẹ Thiên Nhiên:

* **$68.2\%$** dữ liệu sẽ rơi vào vùng $[\mu - \sigma, \mu + \sigma]$.
* **$95.4\%$** dữ liệu rơi vào vùng $[\mu - 2\sigma, \mu + 2\sigma]$.
* **$99.7\%$** dữ liệu rơi vào vùng $[\mu - 3\sigma, \mu + 3\sigma]$.

$\rightarrow$ *Ứng dụng AI:* Khi bro làm tiền xử lý dữ liệu (Data Preprocessing), nếu thấy một điểm dữ liệu nằm cách xa mức trung bình quá $3\sigma$ (tức là rơi vào vùng $0.3\%$ hiếm hoi kia), hệ thống AI sẽ tự động dán nhãn nó là **Outlier (Dữ liệu ngoại lai/Nhiễu)** và thẳng tay xóa nó đi để mô hình không bị học lệch!

---

### 3. Phân phối Nhị thức (Binomial Distribution) - Dành cho AI Classification

Đây là phân phối dành cho **Biến rời rạc** (Chỉ có kết quả Đúng/Sai, 0/1).

**Bài toán:** Tung một đồng xu (xác suất ngửa là $p$) lặp lại $n$ lần. Xác suất để có đúng $k$ lần ngửa là bao nhiêu?

**Công thức PMF (Hàm khối lượng xác suất):**


$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$

* $\binom{n}{k}$ (Tổ hợp chập $k$ của $n$): Số cách sắp xếp các mặt ngửa. Tính bằng $\frac{n!}{k!(n-k)!}$.
* $p^k$: Xác suất của $k$ lần Thành công.
* $(1-p)^{n-k}$: Xác suất của những lần còn lại Thất bại.

$\rightarrow$ *Ứng dụng AI:* Mạng nơ-ron phân loại ảnh Chó/Mèo sử dụng hàm **Cross-Entropy Loss**, và toán học đứng sau cái hàm Loss đó được xây dựng trực tiếp từ chính công thức Binomial này! (Nó cố gắng tối đa hóa xác suất $p$ để trùng khớp với nhãn thật $k$).

---

### 🎮 Bài Tập Thực Chiến: Code Chứng Minh Toán Học

Ở trường đại học, sinh viên phải dùng Tích phân để chứng minh quy tắc 68%. Nhưng ở thế giới AI, chúng ta dùng Numpy và phương pháp **Monte Carlo (Mô phỏng ngẫu nhiên)** để chứng minh nó.

**Nhiệm vụ của bro:**
Viết một script Python thực hiện các bước sau:

1. Tạo ra một thành phố giả lập có $N = 100,000$ người.
2. Sử dụng hàm `np.random.normal(loc, scale, size)` để khởi tạo ngẫu nhiên chiều cao của 100,000 người này.
* Set Kỳ vọng (`loc` = $\mu$) là `170` (cm).
* Set Độ lệch chuẩn (`scale` = $\sigma$) là `5` (cm).
* Gán vào biến `chieu_cao`.


3. Tìm ra 2 ranh giới: `can_duoi = 170 - 5` và `can_tren = 170 + 5`.
4. Dùng mặt nạ Numpy (Boolean Indexing) để lọc ra những người có chiều cao nằm trong khoảng `[can_duoi, can_tren]`.
5. Đếm xem có bao nhiêu người nằm trong khoảng đó, chia cho tổng số người ($100,000$) rồi nhân $100$ để ra phần trăm.

