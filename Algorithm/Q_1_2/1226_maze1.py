from collections import deque

for _ in range(10):
    test_case = int(input())
    maze = [list(map(int, input().strip())) for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sy, sx = i, j
            elif maze[i][j] == 3:
                ey, ex = i, j
    visited = [[0] * 16 for _ in range(16)]
    q = deque()
    q.append((sy, sx))
    visited[sy][sx] = 1

    is_pos = False

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    while q :
        y, x = q.popleft()

        if maze[y][x] == 3:
            is_pos = True
            break

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < 16 and 0 <= nx < 16:
                if visited[ny][nx] != 1 and maze[ny][nx] != 1:
                    visited[ny][nx] = 1
                    q.append((ny, nx))
    
    print(f'#{test_case} {1 if is_pos else 0}')
