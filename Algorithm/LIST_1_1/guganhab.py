T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    K = list(map(int, input().split()))
    gug_sum = sum(K[0:M])
    maax = gug_sum
    miin = gug_sum
    for i in range(1,N-M+1):
        gug_sum = sum(K[i:i+M])
        if gug_sum > maax:
            maax = gug_sum
        if gug_sum < miin:
            miin = gug_sum

    result = maax - miin
    print(f'#{test_case} {result}')
'''
T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    K = list(map(int, input().split()))
    gug_sum = sum(K[0:M])
    maax = gug_sum
    miin = gug_sum
    for i in range(M, N):
        gug_sum += K[i]
        gug_sum -= K[i-M]
        if gug_sum > maax:
            maax =gug_sum
        if gug_sum < miin:
            miin = gug_sum
'''