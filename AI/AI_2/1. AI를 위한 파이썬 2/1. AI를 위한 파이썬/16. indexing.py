import pandas as pd

data = {'이름': ['철수', '영희', '민준', '지아', '서준'],
        '학년': [2, 3, 1, 3, 2],
        '과목': ['수학', '영어', '수학', '영어', '과학'],
        '점수': [85, 92, 78, 88, 95]}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# 인덱스 이름이 'b'인 행 선택
print(df.loc['b'], '\n')

# 인덱스 이름이 'a'부터 'c'까지인 행들 선택 (c 포함!)
print(df.loc['a':'c'], '\n')

# 0번째 위치의 행 선택 (첫 번째 행)
print(df.iloc[0], '\n')

# 0번째부터 3번째 이전까지 (0, 1, 2) 위치의 행들 선택 (3 미포함!)
print(df.iloc[0:3], '\n')

# '이름' 열만 선택
names = df['이름']
print(names, '\n')

# '이름'과 '점수' 열 선택
info = df[['이름', '점수']]
print(info, '\n')

# 인덱스 이름이 'b'인 행 선택
print(df.loc['b'], '\n')

# 인덱스 이름이 'a'부터 'c'까지인 행들 선택 (c 포함!)
print(df.loc['a':'c'], '\n')

# 0번째 위치의 행 선택 (첫 번째 행)
print(df.iloc[0], '\n')

# 0번째부터 3번째 이전까지 (0, 1, 2) 위치의 행들 선택 (3 미포함!)
print(df.iloc[0:3], '\n')

# 인덱스 'c'인 학생의 '과목' 정보
subject_c = df.loc['c', '과목']
print(f"\n인덱스 'c' 학생의 과목: {subject_c}", )

# 1, 2번 행과 0, 2번 열에 해당하는 데이터 조각 선택
sub_df = df.iloc[[1, 2], [0, 2]]
print(sub_df)