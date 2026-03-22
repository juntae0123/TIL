from collections import deque
T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    maze = [list(map(int, input().strip()))for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j
            if maze[i][j] ==3:
                ey, ex = i, j

    q = deque([(sy, sx)])
    visited = [[-1]* N for _ in range(N)]
    visited[sy][sx] = 0

    is_pos = False

    distance = 0

    dy=[1, -1, 0, 0]
    dx=[0, 0, 1, -1]

    while q:
        y, x = q.popleft()

        if maze[y][x] == 3:
            is_pos =True
            distance = visited[y][x] - 1
            break

        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < N and 0 <= nx < N and maze[ny][nx] != 1:
                if visited[ny][nx] == -1:
                    visited[ny][nx] = visited[y][x] + 1
                    q.append((ny, nx))
        
        
    print(f'#{test_case} {distance}')
