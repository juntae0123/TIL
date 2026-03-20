import pandas as pd

data = {'과목': ['영어', '수학', '과학', '사회', '국어'],
        '점수': [92, 78, 88, 95, 100],
        '응시자 수': [200, 150, 180, 210, 220]}
df = pd.DataFrame(data)

print(df.describe())

print(df)
print()
print(df.head(3)) # 처음 3개 행만 보기
print()
print(df.tail(3)) # 마지막 3개 행만 보기

print(df.info())  # 데이터프레임 요약 정보

print(df.describe())  # 수치형 열에 대한 요약 통계

# (행 개수, 열 개수)
print(df.shape)  # (5, 3)

# 열 이름들 
print(df.columns)  # Index(['과목', '점수', '응시자 수'], dtype='object')

# 행 인덱스들
print(df.index)  # RangeIndex(start=0, stop=5, step=1)