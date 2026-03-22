T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    gug = list(map(int, input().split()))
    
    current_s = sum(gug[0:M])
    max_sum = current_s
    min_sum = current_s

    for i in range(1, N - M +1):
        current_s = current_s - gug[i - 1] + gug[i-1 +M]

        if current_s > max_sum:
            max_sum = current_s
        if current_s < min_sum:
            min_sum = current_s
    cha = max_sum - min_sum
    print(f'#{test_case} {cha}')       

