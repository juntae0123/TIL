T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    maze = [list(map(int, input().strip())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                sy, sx = i, j
            elif maze[i][j] == 3:
                ey, ex = i, j
    
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]

    stack = [(sy, sx)]
    visited = [[0]* N for _ in range(N)]
    visited[sy][sx] = 1

    result = 0

    while stack:
        y, x =stack.pop()

        if y == ey and x == ex:
            result = 1
            break       
        
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
      
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue

            if visited[ny][nx] == 1:
                continue

            if maze[ny][nx] != 1 :
                visited[ny][nx] = 1
                stack.append((ny, nx))

    print(f'#{test_case} {result}')

