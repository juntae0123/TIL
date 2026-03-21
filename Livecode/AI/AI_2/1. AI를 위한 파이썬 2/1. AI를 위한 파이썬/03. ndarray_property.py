import numpy as np

data = [[1, 2, 3],
        [4, 5, 6]]

arr = np.array(data)

print(arr, '\n')

print(f"차원: {arr.ndim}")
print(f"모양: {arr.shape}")
print(f"원소 개수: {arr.size}")
print(f"데이터 타입: {arr.dtype}")


