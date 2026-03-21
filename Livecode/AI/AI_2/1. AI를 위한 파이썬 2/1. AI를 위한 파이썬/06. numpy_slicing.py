import numpy as np

arr2d = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])

# 첫 두 행과 1열부터 2열까지
sub_arr = arr2d[:2, 1:3]
# [[2 3]
#  [6 7]]

# 특정 행 전체를 가져오기
row = arr2d[1, :]  # [5 6 7 8]

# 1. 파이썬 예시 
python_list = [10, 20, 30, 40, 50]

sliced_list = python_list[1:4]  # [20, 30, 40]
sliced_list[0] = 999

print(python_list)  # 변경되지 않음 ( [10, 20, 30, 40, 50])

# 1. 넘파이 예시
numpy_array = np.array([10, 20, 30, 40, 50])

sliced_array_view = numpy_array[1:4]  # [20 30 40]
sliced_array_view[0] = 999

print(numpy_array)  # 변경 됨([ 10 999  30  40  50])


