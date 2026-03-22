T = int(input())
for test_case in range(1 , 1 + T):
    N = int(input())
    dalpeng = [[0]*N for _ in range(N)]

    dy = [0, 1, 0,- 1]
    dx = [1, 0, -1, 0]
    
    init = 1
    d = 0
    
    y, x = 0, 0
    
    while init <= N**2:
        dalpeng[y][x] = init
        init += 1

        ny = y + dy[d]
        nx = x + dx[d]
            
        if (ny < 0 or ny >= N or
            nx < 0 or nx >= N or
            dalpeng[ny][nx] != 0):
            d = (d + 1) % 4
            ny = y + dy[d]
            nx = x + dx[d]
        y, x = ny, nx

    print(f'#{test_case}')
    for row in dalpeng:
        print(*row)
