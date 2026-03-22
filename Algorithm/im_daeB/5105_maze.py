from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 시작/도착 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j
            elif maze[i][j] == 3:
                ey, ex = i, j

    dist = [[-1] * N for _ in range(N)]
    q = deque()
    q.append((sy, sx))
    dist[sy][sx] = 0

    while q:
        y, x = q.popleft()
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0 <= ny < N and 0 <= nx < N:
                if maze[ny][nx] != 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    q.append((ny, nx))


    if dist[ey][ex] == -1:
        answer = 0
    else:
        answer = dist[ey][ex] - 1

    print(f"#{test_case} {answer}")
