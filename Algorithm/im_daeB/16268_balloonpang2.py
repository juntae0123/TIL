T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    pan = [list(map(int, input().split())) for _ in range(N)]
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    max_hap = 0

    for i in range(N):
        for j in range(M):
            hap = pan[i][j]

            for k in range(4):
                ny = dx[k] + i
                nx = dy[k] + j
                if  0 <= ny < N and 0 <= nx < M:
                    hap += pan[ny][nx]
            if max_hap <= hap:
                max_hap = hap
    print(f'#{test_case} {max_hap}')