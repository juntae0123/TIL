for _ in range(10):
    tc = int(input())
    maze = [list(map(int, input().strip())) for _ in range(100)]

    for i in range(100):
        for j in range(100):
            if maze[i][j] == 2:
                sy, sx = i, j

    stack = [(sy, sx)]
    visited = [[0]*100 for _ in range(100)]
    visited[sy][sx] = 1

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]
    is_pos = 0

    while stack:
        y, x = stack.pop()
        if maze[y][x] == 3:
            is_pos = 1
            break

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < 100 and 0 <= nx < 100:
                if maze[ny][nx] != 1 and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    stack.append((ny, nx))

    print(f'#{tc} {is_pos}')
