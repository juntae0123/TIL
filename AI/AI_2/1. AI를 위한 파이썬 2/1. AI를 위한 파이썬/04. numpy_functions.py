import numpy as np

# 1. np.zeros(): 모든 원소가 0인 배열 생성
# 2행 4열의 모양으로, 모든 값이 0인 float 타입의 배열을 만듭니다.
zeros_array = np.zeros((2, 4))
print(zeros_array, '\n')
"""
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
"""

# 2. np.ones(): 모든 원소가 1인 배열 생성
# 3행 3열의 모양으로, 모든 값이 1인 integer(정수) 타입의 배열을 만듭니다.
ones_array = np.ones((3, 3), dtype=int)
print(ones_array, '\n')
"""
[[1 1 1]
 [1 1 1]
 [1 1 1]]
"""

# 3. np.full(): 지정한 모양의 배열을 만들고 ,값을 채우기 
# 2행3열의 모양으로, 모든 값이 2인 배열을 생성
full_array = np.full((2, 3), 2)
print(full_array)
"""
[[2 2 2]
 [2 2 2]]
"""

# 4. np.arange(): 연속적인 값을 가진 배열 생성
# 10부터 30 이전까지 5씩 건너뛰는 숫자로 배열을 만듭니다.
arange_array = np.arange(10, 30, 5)
print(arange_array, '\n')  
"""
[10 15 20 25]
"""

# 5. np.linspace(): 균일한 간격을 가진 배열 생성
# 0부터 1까지의 구간을 총 5개의 원소로 균일하게 나눕니다. 
linspace_array = np.linspace(0, 1, 5)
print(linspace_array, '\n')  
"""
[0.   0.25 0.5  0.75 1.  ]     
"""


