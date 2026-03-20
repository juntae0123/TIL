import numpy as np

# 1. np.sqrt() : 배열의 각 요소에 제곱근을 계산
arr_basic = np.array([1, 4, 9, 16])
sqrt_result = np.sqrt(arr_basic)
print("## 1. np.sqrt() 결과 (제곱근) ##")
print(sqrt_result, '\n') # [1. 2. 3. 4.]

# 2. np.exp() : 배열의 각 요소에 지수 함수(e^x)를 적용
# e^0=1, e^1=2.718..., e^2=7.389...
arr_exp = np.array([0, 1, 2])
exp_result = np.exp(arr_exp)
print("## 2. np.exp() 결과 (지수 함수) ##")
print(exp_result, '\n')

# 3. np.log() : 배열의 각 요소에 자연로그(ln)를 계산
# np.exp()의 결과값을 다시 넣으면 원래 값이 나옵니다 (log(e^x) = x)
log_result = np.log(exp_result)
print("## 3. np.log() 결과 (자연로그) ##")
print(log_result, '\n') # [0. 1. 2.]

# 4. np.sin() : 배열의 각 요소에 사인(sin) 값을 계산
# sin(0)=0, sin(90도)=1, sin(180도)=0
arr_angles = np.array([0, np.pi/2, np.pi]) # 0, 90도, 180도를 라디안으로 표현
sin_result = np.sin(arr_angles)
print("## 4. np.sin() 결과 (사인 값) ##")
print(sin_result, '\n') # [0.0000000e+00 1.0000000e+00 1.2246468e-16]
# 참고: np.pi가 완벽한 무한소수가 아니므로 sin(pi)의 결과가 
# 0이 아닌 아주 작은 값으로 나올 수 있습니다.

import numpy as np

# 5. 3x3 크기의 단위 행렬 생성
identity_matrix = np.eye(3)
print(identity_matrix)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# 6. 2행 3열 크기의 배열을 생성하고 난수로 채우기
random_matrix = np.random.randn(2, 3)
print(random_matrix)
# [[-0.53689437  1.23293836 -0.2343209 ],
#  [ 0.8310389   0.38950982 -0.6869436 ]]


# 7. 내적 
# 2x3 행렬 A 생성
matrix_a = np.array([[1, 2, 3],
                     [4, 5, 6]]) # shape: (2, 3)

# 3x2 행렬 B 생성
matrix_b = np.array([[7, 8],
                     [9, 10],
                     [11, 12]]) # shape: (3, 2)

# 행렬 곱 계산 (A @ B 와 동일)
result_matrix = np.dot(matrix_a, matrix_b) # 결과 shape: (2, 2)
print(result_matrix)
# [[ 58  64]
#  [139 154]]

