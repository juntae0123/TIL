T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sqa= []
    for _ in range(N):
        sqa.append(list(map(int, input().split())))

    dy = [1, -1, 0, 0]
    dx = [0, 0, -1, 1]

    start = 10 **9
    max_cnt = 0
    for i in range(N):
        for j in range(N):
            sy, sx = i, j

            cnt = 1


            stack = [(i, j)]


            while stack:
                y, x  = stack.pop()


                for k in range(4):
                    ny = y + dy[k]
                    nx = x + dx[k]
                    if 0 <= ny < N and 0 <= nx < N:
                        if sqa[ny][nx] == sqa[y][x] + 1:
                            stack.append((ny, nx))

                            cnt += 1
                            break
            if cnt > max_cnt:
                max_cnt = cnt
                start = sqa[i][j]
            elif cnt == max_cnt:
                if sqa[i][j] < start:
                    start = sqa[i][j]

    print(f'#{tc} {start} {max_cnt}')