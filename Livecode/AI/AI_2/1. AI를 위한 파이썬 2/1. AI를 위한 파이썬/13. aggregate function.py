import numpy as np

arr = np.array([0, 10, 20, 30, 40])

# 주요 집계 함수 예시
print(f"합계 (sum): {np.sum(arr)}")  # 100
print(f"평균 (mean): {np.mean(arr)}")  # 20.0
print(f"최댓값 (max): {np.max(arr)}")  # 40
print(f"최솟값 (min): {np.min(arr)}")  # 0
print(f"표준편차 (std): {np.std(arr):.2f}")  # 14.14
print(f"분산 (var): {np.var(arr)}")  # 200.0
print(f"최댓값의 인덱스 (argmax): {np.argmax(arr)}")  # 4
print(f"최솟값의 인덱스 (argmin): {np.argmin(arr)}")  # 0


arr2d = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

# 1. 전체 합계 (axis 지정 안 함)
total_sum = arr2d.sum() # 또는 np.sum(arr2d)
print(f"전체 합계: {total_sum}") # 1+2+...+9 = 45

# 2. axis=0 (열 기준 합계)
sum_axis_0 = arr2d.sum(axis=0)
print(f"열(axis=0) 기준 합계: {sum_axis_0}") # [12 15 18]

# 3. axis=1 (행 기준 합계)
# [1+2+3, 4+5+6, 7+8+9]
print(f"행(axis=1) 기준 합계: {sum_axis_1}") # [ 6 15 24]

# 4. 각 열에서 최댓값의 인덱스 찾기
# [0, 0, 0] 열: 7 (인덱스 2)
# [1, 1, 1] 열: 8 (인덱스 2)
# [2, 2, 2] 열: 9 (인덱스 2)
max_indices = np.argmax(arr2d, axis=0)
print(f"각 열의 최댓값 인덱스: {max_indices}") # [2 2 2]

