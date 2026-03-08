T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    dal = [[0]*N for _ in range(N)]
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x, y = 0, 0
    d = 0
    num = 1

    for _ in range(N*N):
        dal[y][x] = num
        num += 1

        nx = x + dx[d]
        ny = y + dy[d]

        if nx <0 or nx >= N or ny <0 or ny >= N or dal[ny][nx] != 0:
            d = (d+1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    print(f'#{test_case}')
    for row in dal:
        print(*row)