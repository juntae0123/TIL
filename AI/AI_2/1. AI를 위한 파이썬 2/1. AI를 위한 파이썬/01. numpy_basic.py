import numpy as np
import time

n = 1_000_000
# 파이썬 리스트
py_list = list(range(n))

# 방법 1: time.time() 사용
start_time = time.time()
result_list = [x * 2 for x in py_list]
end_time = time.time()
print(f"파이썬 리스트 실행 시간: {end_time - start_time:.6f} 초")


# NumPy 배열
np_array = np.arange(n)

start_time = time.time()
result_array = np_array * 2 # 모든 요소에 2를 곱하는 연산
end_time = time.time()
print(f"NumPy 배열 실행 시간: {end_time - start_time:.6f} 초")


