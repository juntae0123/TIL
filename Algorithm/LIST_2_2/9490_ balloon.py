T = int(input())
for test_case in range(1, 1 + T):
    N, M = list(map(int, input().split()))
    balloon = []
    balloon.append([0]*(M+2))
    balloon_best = 0
    for _ in range(N):
        row = [0] + list(map(int, input().split())) + [0]
        balloon.append(row)
    balloon.append([0]*(M+2))
    for i in range(1, N+1):
        for j in range(1, M+1):
            p = balloon[i][j]
            balloon_sum = p

            for x in range(1, p+1):
                if 1 <= i + x <= N : balloon_sum += balloon[i + x][j]
                if 1 <= i - x <= N : balloon_sum += balloon[i - x][j]
                if 1 <= j + x <= M : balloon_sum += balloon[i][j + x]
                if 1 <= j - x <= M : balloon_sum += balloon[i][j - x]
            if balloon_best < balloon_sum:
                balloon_best = balloon_sum

    print(f'#{test_case} {balloon_best}')

