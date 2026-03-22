T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    miro = []
    for _ in range(N):
        miro.append(list(map(int, input().strip())))

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range (N):
        for j in range(N):
            if miro[i][j] == 2:
                sy, sx = i, j

    stack = [(sy, sx)]
    visited = [[0]*N for _ in range(N)]
    visited[sy][sx] = 1

    result = 0

    while stack:
        y, x = stack.pop()

        if miro[y][x] == 3:
            result = 1
            break

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]

            if 0 <= ny < N and 0 <= nx < N:
                if not visited[ny][nx] and miro[ny][nx] != 1:
                    visited[ny][nx] = 1
                    stack.append((ny, nx))
    print(f'#{test_case} {result}')




