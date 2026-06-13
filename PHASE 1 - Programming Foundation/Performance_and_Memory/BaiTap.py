import random
import copy
def bai1(batch_size, data):
    for  i in range(0,len(data) ,batch_size):
        yield data[i:i+batch_size]
import copy

if __name__ == "__main__":
    data = random.sample(range(0,100),20)
    batch_size = 10
    bai1 = bai1(batch_size, data)
    print(list(bai1))
    base_config = {
    "model_name": "CNN",
    "layers": [64, 128, 256],  # List nằm bên trong Dict
    "learning_rate": 0.001
}

# Bro muốn tạo config_2 để thử nghiệm, giữ nguyên mọi thứ nhưng đổi layer cuối
    config_2 = copy.deepcopy(base_config) # Đang dùng Shallow Copy
    config_2["layers"][2] = 512
    print("Base Config:", base_config)
    print("Config 2:", config_2)