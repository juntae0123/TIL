import pandas as pd

# 예시 데이터프레임 생성(ditionary 이용)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "Score": [85.5, 90.3, 78.9]
}

df = pd.DataFrame(data)
print(df)

# 예시 데이터프레임 생성(list와 columns 활용)
data_list = [
    ["David", 28, 88.0],
    ["Eva", 22, 92.5],
    ["Frank", 33, 79.5]
]
columns = ["Name", "Age", "Score"]
df2 = pd.DataFrame(data_list, columns=columns)
print(df2)

