T = int(input())
for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    flies = []
    for _ in range(N):
        flies.append(list(map(int, input().split())))
    best = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            sum_flies = 0
            for x in range(i, i+M):
                for y in range(j, j+M):
                    sum_flies += flies[x][y]
            if sum_flies > best:
                best = sum_flies
    print(f'#{test_case} {best}')
