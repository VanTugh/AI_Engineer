### 1. Giải mã Công thức Vĩ đại: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$

Thay vì dùng A và B chung chung, hãy ráp nó vào bài toán AI. Cụ thể là đi tìm **Giả thuyết (Hypothesis - H)** dựa trên **Dữ liệu/Bằng chứng (Evidence - E)**. Công thức trở thành:


$$P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}$$

Bộ ba thuật ngữ làm nên tên tuổi của định lý này gồm:

* **Prior ($P(H)$ - Niềm tin ban đầu):** Những gì hệ thống AI tin tưởng *trước khi* nhìn thấy dữ liệu mới. (Ví dụ: Dựa trên lịch sử, tỷ lệ email rác luôn là 30%).
* **Likelihood ($P(E|H)$ - Độ hợp lý):** Nếu giả thuyết đó là đúng, thì khả năng quan sát được bằng chứng này là bao nhiêu? (Ví dụ: Nếu thư ĐÚNG là rác, thì xác suất có chữ "Khuyến mãi" là 70%). AI Model sẽ "học" cái Likelihood này từ tập Training Data.
* **Posterior ($P(H|E)$ - Niềm tin cập nhật):** Cái đích cuối cùng. Sau khi kết hợp niềm tin ban đầu và bằng chứng vừa thu thập, AI sẽ chốt lại xác suất mới là bao nhiêu.

### 2. Bayesian Updating (Cập nhật Bayes - Vòng lặp học tập)

Đây là cơ chế giúp AI "thông minh lên" theo thời gian thực (Online Learning).

* **Nguyên lý:** *Posterior của ngày hôm nay chính là Prior của ngày mai.*
* **Ví dụ thực tế:** Bro đang làm một hệ thống xe tự lái.
* Bước 1: Hệ thống thấy một bóng đen mờ mờ trong sương mù. **Prior:** "Khả năng cao đó là cột đèn" (Vì cao tốc toàn cột đèn).
* Bước 2: Xe tiến gần hơn một chút, thu thập được **Evidence** mới: "Cái bóng đen đó vừa di chuyển".
* Bước 3: **Bayesian Updating** kích hoạt! Nó tính ra **Posterior**: "Xác suất là con người băng qua đường tăng vọt lên 90%".
* Bước 4: Cái 90% này lập tức trở thành **Prior mới** cho giây tiếp theo, xe quyết định phanh gấp!



### 3. Naive Bayes: Ứng dụng thực chiến trực tiếp

Định lý Bayes cực hay, nhưng có một điểm yếu: Nó chỉ làm việc tốt với 1 bằng chứng (1 từ khóa). Nếu email có 100 từ khóa khác nhau: "Khuyến", "mãi", "trúng", "thưởng", "Click",... thì sao?

Tính $P(W_1, W_2, ... W_{100} | \text{Spam})$ theo toán học chặt chẽ là một bài toán bất khả thi vì đòi hỏi bộ nhớ khổng lồ. Và đây là lúc sự "ngây thơ" (Naive) cứu cánh cả hệ thống!

* **Giả định Naive (Ngây thơ):** Thuật toán tự "lừa" bản thân rằng sự xuất hiện của các từ trong câu là **hoàn toàn độc lập** với nhau. Việc có chữ "Trúng" không liên quan gì đến việc có chữ "Thưởng".
* **Công thức "Ăn gian":** Thay vì tính chung một cụm phức tạp, nó tách nhỏ ra và nhân dồn lại:

$$P(W_1, W_2 | \text{Spam}) = P(W_1 | \text{Spam}) \cdot P(W_2 | \text{Spam})$$


* **Bí quyết tối ưu của AI Engineer:** Khi so sánh xem email là Spam hay Normal, AI không thèm tính cái Mẫu số $P(E)$ (Xác suất toàn phần). Tại sao? Vì mẫu số của hai bên là y hệt nhau! Nó chỉ cần tính cái Tử số (Tích của Prior và các Likelihood) rồi so sánh xem bên nào to hơn là chốt đơn. Công thức rút gọn trở thành tỷ lệ thuận ($\propto$):

$$P(\text{Spam} | \text{Text}) \propto P(\text{Spam}) \cdot P(W_1 | \text{Spam}) \cdot P(W_2 | \text{Spam}) \dots$$



---

### 🎮 Bài Tập Thực Chiến: Xây dựng AI Classifier bằng Naive Bayes

Không cần dùng Scikit-Learn, bro sẽ tự tay ráp nối công thức cốt lõi của Naive Bayes bằng Python.

**Kịch bản:**
Có một email mới bay vào hòm thư, nội dung chỉ gồm 2 từ: **"Trúng thưởng"**.
Hệ thống Database trước đó đã trích xuất được bộ thông số (Prior và Likelihood) như sau:

* $P(\text{Spam}) = 0.4$
* $P(\text{Normal}) = 0.6$
* $P(\text{"Trúng"} | \text{Spam}) = 0.8$
* $P(\text{"Thưởng"} | \text{Spam}) = 0.7$
* $P(\text{"Trúng"} | \text{Normal}) = 0.1$
* $P(\text{"Thưởng"} | \text{Normal}) = 0.05$

**Nhiệm vụ của bro:**
Viết một đoạn code Python thực hiện các yêu cầu sau:

1. Tính điểm `score_spam` (Tử số của Bayes cho trường hợp Spam) bằng công thức: $P(\text{Spam}) \cdot P(\text{"Trúng"} | \text{Spam}) \cdot P(\text{"Thưởng"} | \text{Spam})$.
2. Tính điểm `score_normal` (Tử số của Bayes cho trường hợp Normal) theo logic tương tự.
3. So sánh `score_spam` và `score_normal`. In ra quyết định cuối cùng xem AI sẽ phân loại email này vào nhãn nào.
