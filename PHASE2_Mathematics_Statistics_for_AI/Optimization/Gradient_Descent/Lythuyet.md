### 1. Cuộc chiến Learning Rate ($\alpha$)

Nhắc lại công thức cốt lõi: $\theta = \theta - \alpha \cdot \nabla L(\theta)$

* **$\alpha$ quá lớn (Too high):** Thuật toán tự tin thái quá. Nó nhảy những bước vĩ đại vượt qua cả cái thung lũng, văng lên sườn núi bên kia, rồi lại văng ngược lại. Kết quả là sai số (Loss) phát nổ (Divergence / Exploding).
* **$\alpha$ quá nhỏ (Too low):** Đi những bước rụt rè bằng hạt cát. Mất hàng năm trời mới lết được xuống đáy (Slow convergence), hoặc tồi tệ hơn là hết thời gian chạy (Timeout) trước khi tới đích.

### 2. Batch GD vs SGD vs Mini-batch (Nghệ thuật nuốt Big Data)

Giả sử bro có 1 triệu bức ảnh chó mèo. Để tính ra cái Gradient $\nabla L$, bro sẽ đưa bao nhiêu ảnh cho AI xem trong một lần học (1 bước nhảy)?

* **Batch Gradient Descent (Ăn cả cái bánh):**
* Ném toàn bộ 1 triệu bức ảnh vào RAM để tính tổng sai số rồi mới đi 1 bước.
* *Ưu điểm:* Bước đi cực kỳ chính xác, nhắm thẳng xuống đáy.
* *Nhược điểm:* **Cháy RAM!** Không có cái GPU nào trên thế giới chứa nổi 1 triệu bức ảnh cùng lúc. Cực kỳ chậm.


* **Stochastic Gradient Descent (SGD - Ăn từng vụn bánh):**
* Bốc ngẫu nhiên đúng 1 bức ảnh, tính sai số, đi 1 bước. Lặp lại 1 triệu lần.
* *Ưu điểm:* Cực nhanh, tốn ít RAM. Quỹ đạo giật cục (Zig-zag) giúp nó vô tình nhảy thoát khỏi Local Minima.
* *Nhược điểm:* Chạy quá "say xỉn", nó cứ nhảy múa loạn xạ quanh cái đáy chứ không chịu dừng hẳn lại. Không tận dụng được sức mạnh tính toán song song của GPU.


* **Mini-batch Gradient Descent (Ăn từng miếng - CHÂN ÁI CỦA DEEP LEARNING):**
* Chia 1 triệu ảnh thành các lô (batch) nhỏ, ví dụ: 32, 64, 128, 256 ảnh. Tính sai số trung bình của 1 lô đó rồi đi 1 bước.
* *Vì sao nó là Vua?* Kích thước 64 hay 128 ảnh nhét vừa vặn vào bộ nhớ VRAM của GPU NVIDIA. GPU sẽ dùng phép nhân Ma trận để tính đạo hàm cho 128 ảnh đó **CÙNG MỘT LÚC** (Vectorization). Vừa nhanh, quỹ đạo vừa đủ mượt, vừa thoát được bẫy!



---

### 🔥 BÀI TẬP TRY HARD: CÀI ĐẶT MINI-BATCH GRADIENT DESCENT (DẠNG MA TRẬN)

Bro nói muốn Try Hard đúng không? Chúng ta sẽ không chơi với 1 biến $x$ nữa.
Bro sẽ code lại thuật toán huấn luyện lõi của Scikit-Learn để tìm trọng số $\theta$ cho mô hình Linear Regression có **3 đặc trưng (features)** và **1000 dòng dữ liệu**.

**Cẩm nang Toán học (Bro cần thuộc nằm lòng):**

1. Mô hình dự đoán: $\hat{y} = X_{batch} \cdot \theta$
*(Kích thước: $(batch\_size, 3) \times (3, 1) \rightarrow (batch\_size, 1)$)*
2. Công thức Đạo hàm của MSE dạng Ma trận:

$$\nabla L = \frac{2}{m_{batch}} X_{batch}^T \cdot (\hat{y} - y_{batch})$$



*(Nó lấy sai số của cả batch nhân ngược với ma trận input $X$ đã chuyển vị)*

**Nhiệm vụ của bro:**
Hãy điền code vào 5 vị trí `TODO` trong đoạn script dưới đây. (Không dùng vòng lặp cho các phép tính toán học, **BẮT BUỘC** dùng phép nhân ma trận `@` của NumPy).

```python
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")

# 1. Giả lập Big Data (1000 dòng, 3 features)
np.random.seed(42)
X_data = np.random.randn(1000, 3) 
# Trọng số thực tế (Mục tiêu mà mô hình phải tự tìm ra)
true_theta = np.array([[1.5], [-2.0], [3.0]]) 
# y = X*theta + nhiễu
y_data = X_data @ true_theta + np.random.randn(1000, 1) * 0.1 

def mini_batch_gd(X: np.ndarray, y: np.ndarray, lr: float = 0.01, epochs: int = 50, batch_size: int = 32):
    m, n = X.shape
    # Khởi tạo ma trận trọng số theta ngẫu nhiên (3 hàng, 1 cột)
    theta = np.random.randn(n, 1) 
    
    for epoch in range(epochs):
        # TODO 1: Shuffle (Xáo trộn) dữ liệu
        # Tạo một mảng indices ngẫu nhiên từ 0 đến m-1
        # Cập nhật lại X và y theo các indices đã xáo trộn
        
        
        # Duyệt qua từng Mini-batch
        for i in range(0, m, batch_size):
            # TODO 2: Cắt lấy X_batch và y_batch có kích thước = batch_size
            
            
            # TODO 3: Tính ma trận dự đoán y_hat (dùng phép nhân ma trận X_batch với theta)
            
            
            # TODO 4: Tính vector Gradient theo công thức: 
            # (2 / batch_size) * (X_batch chuyển vị) nhân ma trận với (y_hat - y_batch)
            
            
            # TODO 5: Cập nhật trọng số theta (Đi ngược hướng gradient)
            

    return theta

if __name__ == "__main__":
    logging.info("Trọng số thật sự của vũ trụ:\n" + str(true_theta))
    logging.info("-" * 40)
    
    learned_theta = mini_batch_gd(X_data, y_data, lr=0.05, epochs=50, batch_size=64)
    
    logging.info("Trọng số do AI học được:\n" + str(learned_theta))
    
    # Kiểm tra xem AI học có sát với thực tế không
    sai_so = np.linalg.norm(learned_theta - true_theta)
    if sai_so < 0.05:
        logging.info("🔥 QUÁ ĐỈNH! Mô hình đã hội tụ cực kỳ chính xác!")
    else:
        logging.info("❌ Mô hình chưa hội tụ. Hãy kiểm tra lại công thức Gradient bằng Ma trận.")

```
