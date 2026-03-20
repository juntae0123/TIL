import pandas as pd
import numpy as np

data = {'이름': ['철수', '영희', '민준', '지아', '서준'],
        '학년': [2, 3, 1, 3, 2],
        '과목': ['수학', '영어', '수학', '영어', '과학'],
        '점수': [85, 92, 78, 88, 95]}

df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# '서준'의 '과목'과 '점수'를 NaN으로 설정
df.loc['e', '과목'] = np.nan
df.loc['e', '점수'] = np.nan

# '학년'이 2학년 또는 3학년인 행 필터링
target_grades = [2, 3]
filt_isin = df['학년'].isin(target_grades)
print(df[filt_isin], '\n')

# '과목'이 NaN인 행 필터링
filt_isnull = df['과목'].isnull()
df_is_null = df[filt_isnull]
print(df_is_null, '\n')  

# '점수'가 NaN이 아닌 행 필터링
filt_notnull = df['점수'].notnull()
df_not_null = df[filt_notnull]
print(df_not_null)


# '점수'가 90점 이상인 행 필터링
filt = df['점수'] >= 90

df_high_score = df[filt]
print(df_high_score, "\n")

# 또는 한 줄로: df_high_score = df[df['점수'] >= 90]

# '과목'이 '수학'이고 '점수'가 80점 이상인 행 필터링
df_seoul_high = df[(df['점수'] >= 80) & (df['과목'] == '수학')]
print(df_seoul_high, "\n")

# '점수'가 92점이거나 '과목'이 '과학'인 행 필터링
df_perfect_or_busan = df[(df['점수'] == 92) | (df['과목'] == '과학')]
print(df_perfect_or_busan, "\n")

# '과목'이 '과학'이 아닌 행 필터링
df_not_seoul = df[~(df['과목'] == '과학')]
print(df_not_seoul, "\n")

