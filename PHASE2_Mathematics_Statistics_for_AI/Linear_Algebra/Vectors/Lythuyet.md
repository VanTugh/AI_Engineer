### 1. Vector là gì? (Geometrically vs Algebraically)

* **Dưới góc độ Hình học (Geometrically):** Vector là một mũi tên bắn ra trong không gian. Nó có 2 thuộc tính: **Độ dài** (mạnh hay yếu) và **Hướng** (chỉ đi đâu).
* **Dưới góc độ Đại số (Algebraically):** Đây là góc nhìn của anh em IT. Vector đơn giản chỉ là một danh sách các con số (một mảng 1 chiều - 1D Array).
* Ví dụ: Một ngôi nhà có 2 phòng ngủ, rộng 50m2, giá 3 tỷ. Ta có một vector đặc trưng (Feature Vector) là $v = [2, 50, 3]$. Mọi dữ liệu trên đời đều bị ép thành dạng mảng này trước khi nạp vào model.



### 2. Các phép toán cơ bản (Addition, Scalar Multiplication)

* **Cộng hai Vector (A + B):** Cộng từng phần tử tương ứng với nhau. Về mặt hình học, nó giống như việc ghép nối đuôi 2 mũi tên lại để tạo ra mũi tên mới.
* **Nhân vô hướng (Scalar Multiplication):** Lấy một số thực nhân với vector (vd: $3 \times v$). Phép này chỉ làm vector "dãn ra" hoặc "co lại" hoặc "quay ngoắt 180 độ" (nếu nhân với số âm), hướng đi của nó (tỉ lệ các phần tử) vẫn giữ nguyên.

### 3. Tích vô hướng (Dot Product) - Linh hồn của AI

Phép nhân 2 ma trận/vector mà bro hay dùng `np.dot(A, B)` chính là nó.

* **Công thức:** $A \cdot B = \sum_{i=1}^{n} a_i b_i$ (Nhân từng cặp tương ứng rồi cộng tổng lại thành một con số duy nhất).
* **Ý nghĩa Hình học (Projection):** Tích vô hướng cho biết mức độ "tương đồng về hướng" của 2 mũi tên. Nó chiếu cái mũi tên A xuống cái mũi tên B xem phần đổ bóng dài bao nhiêu. Trong mạng Neural Network, các phép tính Weights nhân với Inputs thực chất là hàng triệu phép Dot Product chạy ngầm.

### 4. Vector Magnitude / Norms (Độ lớn của Vector)

Để đo chiều dài của cái mũi tên vector, ta dùng khái niệm **Norm** (Ký hiệu là $||v||$). Trong Machine Learning, Norm thường được dùng để tính sai số (Loss function) giữa dự đoán và thực tế.

* **L2 Norm (Euclidean):** Khoảng cách đường chim bay (đường thẳng). Công thức lấy căn bậc 2 của tổng bình phương: $||v||_2 = \sqrt{v_1^2 + v_2^2 + ... + v_n^2}$.
* **L1 Norm (Manhattan):** Khoảng cách đi theo hình dích dắc (như đi dọc theo các tòa nhà trong thành phố). Tính bằng tổng các giá trị tuyệt đối: $||v||_1 = |v_1| + |v_2| + ... + |v_n|$.
* **Lp Norm:** Công thức tổng quát cho L1, L2.

### 5. Unit Vectors & Normalization (Chuẩn hóa)

* **Unit Vector (Vector đơn vị):** Là vector có độ dài (L2 Norm) chính xác bằng 1.
* **Normalization:** Khi làm AI, dữ liệu nhà (giá 3 tỷ) và số phòng (2 phòng) có thang đo quá lệch nhau, model sẽ bị ngợp. Ta phải "chuẩn hóa" bằng cách lấy vector ban đầu chia cho chính độ dài L2 của nó: $\hat{v} = \frac{v}{||v||}$. Mũi tên lúc này giữ nguyên hướng nhưng bị thu ngắn lại đúng bằng 1.

### 6. Cosine Similarity & Embeddings (Bí mật của ChatGPT)

Đây là kiến thức đáng tiền nhất trong mục này! Trong xử lý ngôn ngữ tự nhiên (NLP), mỗi từ hoặc mỗi câu được AI dịch thành một vector khổng lồ (gọi là **Embedding**).

* Để biết 2 câu văn có nét nghĩa giống nhau không, AI không đo bằng khoảng cách L2, mà đo bằng **Góc** giữa 2 mũi tên vector.
* **Công thức:** $\cos(\theta) = \frac{A \cdot B}{||A|| \times ||B||}$
* Kết quả dao động từ -1 đến 1. Nếu $\cos(\theta)$ càng gần 1, hai từ đó càng giống nghĩa nhau (VD: "King" và "Queen").

### 7. Orthogonality (Tính trực giao)

* Khi $\cos(\theta) = 0$, nghĩa là 2 mũi tên vuông góc với nhau (90 độ).
* Về mặt toán học: Tích vô hướng (Dot Product) của chúng bằng 0.
* Về mặt ý nghĩa AI: Hai dữ liệu này **không có bất kỳ mối tương quan nào** với nhau (Ví dụ: Từ "Xe đạp" và từ "Con cá").

---

### 🎮 Bài Tập Thực Chiến: Xây dựng hệ thống đo lường ngữ nghĩa

Hãy vận dụng ngay kỹ năng Numpy của bro để mã hóa các khái niệm toán học này thành code.

**Kịch bản:** Hệ thống AI vừa nhúng (embed) 3 từ khóa thành 3 vector tọa độ 1D (đã đơn giản hóa) như sau:

* `word_apple = np.array([3, 4])`
* `word_banana = np.array([4, 3])`
* `word_car = np.array([-4, 3])`

**Nhiệm vụ của bro:**
Viết một script Python sử dụng thư viện `numpy` (không dùng hàm `cosine_similarity` xây sẵn của Scikit-learn):

1. Tính độ lớn (**L2 Norm**) của vector `word_apple` (Gợi ý: Dùng `np.linalg.norm`).
2. Tính Tích vô hướng (**Dot Product**) giữa `word_apple` và `word_banana`.
3. Tự viết một hàm `compute_cosine(v1, v2)` dựa trên công thức toán học ở mục 6.
4. Dùng hàm vừa viết để tính Cosine Similarity giữa cặp `(apple, banana)` và cặp `(apple, car)`. In kết quả ra và đưa ra nhận xét: Cặp nào có nét nghĩa tương đồng hơn, cặp nào vuông góc (Orthogonal)?