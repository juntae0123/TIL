import numpy as np

data = np.array([[1, 2], 
                 [3, 4], 
                 [5, 6]])

# 조건에 맞는 boolean 배열 생성
bool_mask = data > 3
print("Boolean 마스크:\n", bool_mask)
# [[False False]
#  [False  True]
#  [ True  True]]

# 마스크를 사용해 True 위치의 값만 추출 (1차원 배열로 반환됨)
print("\n3보다 큰 값들:", data[bool_mask]) # 출력: [4 5 6]

# 조건을 직접 인덱스에 넣어도 동일하게 동작합니다.
print("짝수만 추출:", data[data % 2 == 0]) # 출력: [2 4 6]

