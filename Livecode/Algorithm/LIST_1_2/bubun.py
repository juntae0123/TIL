def yesorno(issu):
    if issu == True:
        return 'YES'
    if issu == False:
        return 'NO'


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    arr1 = list(map(int,input().split()))
    arr2 = list(map(int,input().split()))
    issu = True
    count = 0

    for ar1 in arr1:
        if count < M and ar1 ==arr2[count]:
            count += 1
            if count == M:
                break
    if count != M:
        issu = False

    print(f'#{test_case} {yesorno(issu)}')


