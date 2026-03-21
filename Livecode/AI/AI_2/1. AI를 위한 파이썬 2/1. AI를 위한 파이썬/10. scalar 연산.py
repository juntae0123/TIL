import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 덧셈: 모든 요소에 10을 더하기
add_result = arr + 10
print("덧셈 결과:\n", add_result)
# [[11 12 13]
#  [14 15 16]]

# 곱셈: 모든 요소에 3을 곱하기
mul_result = arr * 3
print("\n곱셈 결과:\n", mul_result)
# [[ 3  6  9]
#  [12 15 18]]


arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# 배열 간 덧셈
add_arr = arr1 + arr2
print("배열 간 덧셈:\n", add_arr)
# [[ 6  8]
#  [10 12]]

# 배열 간 곱셈
mul_arr = arr1 * arr2
print("\n배열 간 곱셈:\n", mul_arr)
# [[ 5 12]
#  [21 32]]

