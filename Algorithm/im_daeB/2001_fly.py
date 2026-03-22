T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(N)]


    max_kill_cnt = 0

    for i in range(N - M+ 1):
        for j in range(N - M + 1):
            kill_cnt = 0
            for k in range(M):
                for a in range(M):
                    kill_cnt += fly[i+k][j+a]
            if kill_cnt > max_kill_cnt:
                max_kill_cnt = kill_cnt
    print(f'#{test_case} {max_kill_cnt}')
