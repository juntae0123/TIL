arr = [1, 2, 3, 4]
n = len(arr)

def get_subset1(target):
    # 1. 0~ 부분집합의 수 만큼 반복
    # - i : 부분 집합의 번호
    for i in range(1 << n):
        for idx in range(n):
            if i & (1 << idx):
                print(arr[idx], end = ' ')
        print()


get_subset1(0)