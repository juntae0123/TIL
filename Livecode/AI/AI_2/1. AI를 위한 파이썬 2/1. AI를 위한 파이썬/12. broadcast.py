import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

# 브로드캐스팅 발생!
result = arr + 5 
print(result)
"""
[[ 6  7  8]
 [ 9 10 11]]
"""
