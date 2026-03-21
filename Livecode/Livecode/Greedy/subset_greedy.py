# 3명의 친구 부분집합 만들기
arr = ['O', 'X']
path = []

# 3명의 친구 : depth = 3
# O, X 중 하나 선택 : branch =2
def recur(cnt):
    if cnt == 3:
        return

    # 0을 선택(부분집합에 포함되는 경우)
    path.append(arr[0])
    recur(cnt + 1)
    path.pop()

    # X를 선택
    path.append(arr[1])
    recur(cnt + 1)
    path.pop()


recur(0)

#-------------------------------------------
# 응용

name = ['MIN', 'CO', 'TIM']

def recur2(idx, subset):
    if idx == 3:
        print(*subset)
        return

    # 부분집합에 포함 하는 경우
    
    recur2(idx + 1, subset + [name[idx]])
    
    # 부분집합에 포함 안 하는 경우

    recur2(idx + 1, subset)

recur2(0, [])