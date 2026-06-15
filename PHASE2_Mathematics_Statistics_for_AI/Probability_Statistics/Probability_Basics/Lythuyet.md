### 1. Sample Space, Events, Outcomes (Không gian mẫu, Biến cố, Kết quả)

* **Outcome (Kết quả - $\omega$):** Là một kết quả đơn lẻ có thể xảy ra. *Ví dụ: Bro bốc ngẫu nhiên một bức ảnh trong tập Dataset, bức ảnh đó là một con "Chó Shiba". Đó là một outcome.*
* **Sample Space (Không gian mẫu - $\Omega$):** Là tập hợp TẤT CẢ các kết quả có thể xảy ra. *Ví dụ: Trong bài toán nhận diện chữ số viết tay (MNIST), không gian mẫu là tập hợp các nhãn $\{0, 1, 2, 3, 4, 5, 6, 7, 8, 9\}$.*
* **Event (Biến cố - $E$):** Là một tập con của Không gian mẫu. *Ví dụ: Biến cố "Bức ảnh là một số chẵn" $\rightarrow E = \{0, 2, 4, 6, 8\}$.*

### 2. Joint, Marginal, Conditional Probability (Bộ ba cốt lõi)

Đây là phần quan trọng nhất bro cần nắm để hiểu cách các mô hình AI dự đoán chuỗi hoặc văn bản.

* **Joint Probability (Xác suất đồng thời - $P(A \cap B)$ hoặc $P(A, B)$):** Xác suất để 2 biến cố A và B xảy ra **cùng một lúc**.
*Ví dụ: Xác suất để một email vừa chứa chữ "Trúng thưởng" (A) VÀ vừa là "Thư rác" (B).*
* **Marginal Probability (Xác suất biên - $P(A)$):** Xác suất để một biến cố A xảy ra mà **mặc kệ** tất cả các biến cố khác. Nó được gọi là "biên" vì trong các bảng dữ liệu 2D, người ta thường cộng tổng các cột/hàng lại và viết kết quả ở "lề" (biên) của bảng.
* **Conditional Probability (Xác suất có điều kiện - $P(A|B)$):** **Linh hồn của Machine Learning!** Trả lời câu hỏi: *"Nếu tôi ĐÃ BIẾT B xảy ra rồi, thì khả năng A xảy ra là bao nhiêu?"*.
* **Công thức:** 
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$


* *AI Context:* Khi ChatGPT sinh ra chữ "Trí tuệ", xác suất để chữ tiếp theo là "Nhân tạo" cực kỳ cao. Đó chính là $P(\text{Nhân tạo} | \text{Trí tuệ})$.



### 3. Independence (Sự độc lập)

* **Toán học:** Hai biến cố A và B được gọi là độc lập nếu việc B xảy ra không làm thay đổi xác suất của A.
* $P(A|B) = P(A)$
* Hoặc: $P(A \cap B) = P(A) \cdot P(B)$


* **AI Context (Thuật toán Naive Bayes):** Trong xử lý ngôn ngữ tự nhiên (NLP) đời đầu, để tính toán cho nhanh, người ta giả định "ngây thơ" (Naive) rằng sự xuất hiện của chữ "Tuyệt" và chữ "Vời" trong một câu là hoàn toàn độc lập với nhau. Dù giả định này sai bét trong thực tế, nhưng nó lại giúp thuật toán chạy cực nhanh trên Big Data và cho kết quả lọc Spam đáng kinh ngạc.

### 4. Law of Total Probability (Định lý Xác suất Toàn phần)

Đôi khi bro không thể tính trực tiếp xác suất của một biến cố B, vì dữ liệu quá lộn xộn. Định lý này cho phép bro "chia để trị": Cắt không gian mẫu thành các mảnh nhỏ (các biến cố $A_i$ độc lập và bao quát hết không gian), tính xác suất trên từng mảnh, rồi cộng dồn lại.

* **Công thức:**

$$P(B) = \sum_{i} P(B | A_i) \cdot P(A_i)$$


* *AI Context:* Khi làm hệ thống gợi ý (Recommender System), để tính xác suất $P(\text{User mua hàng})$, hệ thống sẽ chia user ra thành các tập nhỏ: (Xác suất mua hàng | là Nam) $\times$ $P(\text{Nam})$ + (Xác suất mua hàng | là Nữ) $\times$ $P(\text{Nữ})$.

---

### 🎮 Bài Tập Thực Chiến: Xây dựng bộ não cho Filter Spam

Hãy khởi động Python và hóa thân thành một kỹ sư Data. Bro được cung cấp tập dữ liệu (dataset) gồm **1000 email**. Phân tích sơ bộ cho thấy:

* Có **300** email là Spam (Thư rác).
* Có **700** email là Normal (Thư bình thường).
* Trong số 300 email Spam, có **210** email chứa từ khóa "Khuyến mãi".
* Trong số 700 email Normal, chỉ có **35** email chứa từ khóa "Khuyến mãi".

**Nhiệm vụ của Intern:**
Không cần dùng thư viện phức tạp, bro hãy tự nhẩm hoặc code vài dòng tính toán cơ bản để tìm ra 3 con số sau:

1. Xác suất biên $P(\text{Spam})$ và $P(\text{Normal})$.
2. Xác suất có điều kiện $P(\text{Từ khóa} | \text{Spam})$ (Nghĩa là: Biết chắc thư này là Spam rồi, thì tỷ lệ xuất hiện từ khóa là bao nhiêu?).
3. Xác suất có điều kiện $P(\text{Từ khóa} | \text{Normal})$.
