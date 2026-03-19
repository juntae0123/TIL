import numpy as np

# arr는 여전히 12개의 원소를 가짐
arr = np.arange(12)

# 1. 1D -> 2D로 변경 (3행 4열)
reshaped_arr = arr.reshape(3, 4)
print("reshape(3, 4) 결과 (2D):\n", reshaped_arr, reshaped_arr.shape)

# 1. 행을 4로 지정하면, 열은 알아서 3으로 계산됨 (4 * 3 = 12)
arr_m1 = arr.reshape(4, -1)
print("\nreshape(4, -1) 결과:\n", arr_m1, arr_m1.shape)

# 2. 열을 2로 지정하면, 행은 알아서 6으로 계산됨 (6 * 2 = 12)
arr_m2 = arr.reshape(-1, 2)
print("\nreshape(-1, 2) 결과:\n", arr_m2, arr_m2.shape)

