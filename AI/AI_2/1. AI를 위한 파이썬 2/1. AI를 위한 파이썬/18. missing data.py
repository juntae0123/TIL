import pandas as pd
import numpy as np

data = {'A': [1, 2, np.nan, 4, 5],
        'B': [6, np.nan, 8, np.nan, 10],
        'C': [11, 12, 13, 14, 15],
        'D': [np.nan, np.nan, np.nan, np.nan, np.nan]}

df = pd.DataFrame(data)
print(df, '\n')
# 결측치(NaN)가 하나라도 있는 행을 제거
df_dropped_rows = df.dropna()
print( df_dropped_rows, '\n')

# 결측치(NaN)가 하나라도 있는 열을 제거
df_dropped_cols = df.dropna(axis=1)
print(df_dropped_cols, '\n')  # 출력 안됨

# 모든 값이 결측치인 행을 제거
df_dropped_all_rows = df.dropna(how='all')
print(df_dropped_all_rows, '\n')

# tips 데이터셋 로드
df = sns.load_dataset('tips')