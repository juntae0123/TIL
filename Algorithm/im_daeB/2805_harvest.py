T = int(input())
for test_case in range(1,1 + T):
    N = int(input())    
    farm = [list(map(int, input().strip())) for _ in range(N)]
    
    mid = N // 2
    harvest = 0

    # 위 + 가운데
    for r in range(mid + 1):
        harvest += sum(farm[r][mid - r : mid + r + 1])

    # 아래
    for r in range(mid + 1, N):
        diff = r - mid
        harvest += sum(farm[r][diff : N - diff])

    print(f'#{test_case} {harvest}')
