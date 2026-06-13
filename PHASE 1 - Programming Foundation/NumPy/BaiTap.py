import numpy as np
def bai1(kwargs: np.ndarray) -> np.ndarray:
    matrix = kwargs.reshape(3,3)
    return np.where(matrix < 0, 0, matrix)
def bai2(y_pred : np.ndarray , y_true : np.ndarray ) -> np.ndarray:
    error_matrix = (y_pred - y_true)**2
    print(error_matrix)
    list_MSE = np.mean(error_matrix, axis=1)
    return list_MSE

if __name__ == "__main__":
    arr = np.array([-2, 1, 5, -5, 8, -1, 3, -4, 0])
    new_matrix = bai1(arr)
    print(new_matrix)

    y_pred = np.array([[0.1, 0.2, 0.6, 0.1], [0.8, 0.1, 0.05, 0.05], [0.2, 0.5, 0.2, 0.1]])
    y_true = np.array([[0, 0, 1, 0], [1, 0, 0, 0], [0, 1, 0, 0]])
    mse = bai2(y_pred, y_true)
    print(mse)
