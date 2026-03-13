import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# SWEA 1953. 탈주범 검거
#
# [풀이 핵심]
# 1. 시작 위치에서 L시간 동안 갈 수 있는 칸의 개수를 구해야 한다.
# 2. "한 시간마다 인접 칸으로 이동" => 최단거리/시간 탐색이므로 BFS 사용
# 3. 단순 상하좌우 이동이 아니라,
#    "현재 칸 터널이 그 방향으로 뚫려 있어야 하고"
#    "다음 칸 터널도 반대 방향으로 뚫려 있어야" 이동 가능
#
# ------------------------------------------------------------
# 방향 인덱스 통일
# 0: 상, 1: 하, 2: 좌, 3: 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 각 방향의 반대 방향
# 상 <-> 하, 좌 <-> 우
opposite = [1, 0, 3, 2]

# 터널 타입별로 이동 가능한 방향
# 문제에서 주어진 구조를 그대로 딕셔너리로 정리
tunnel = {
    1: [0, 1, 2, 3],  # 상 하 좌 우
    2: [0, 1],        # 상 하
    3: [2, 3],        # 좌 우
    4: [0, 3],        # 상 우
    5: [1, 3],        # 하 우
    6: [1, 2],        # 하 좌
    7: [0, 2],        # 상 좌
}


def bfs(start_y, start_x):
    # 방문 배열
    # visited[y][x] = 그 칸에 처음 도착한 시간
    # 시작 위치는 "1시간째에 존재"하므로 1로 시작
    visited = [[0] * M for _ in range(N)]
    visited[start_y][start_x] = 1

    q = deque()
    q.append((start_y, start_x))

    # 시작 위치도 포함하므로 답은 1개부터 시작
    count = 1

    while q:
        y, x = q.popleft()

        # 현재 칸에 도착한 시간이 이미 L이면
        # 더 이동하면 L시간을 넘어가므로 확장하지 않음
        if visited[y][x] == L:
            continue

        # 현재 칸의 터널 타입
        cur_type = board[y][x]

        # 현재 터널에서 갈 수 있는 방향들만 확인
        for d in tunnel[cur_type]:
            ny = y + dy[d]
            nx = x + dx[d]

            # 1. 범위 밖이면 이동 불가
            if not (0 <= ny < N and 0 <= nx < M):
                continue

            # 2. 다음 칸에 터널이 없으면 이동 불가
            if board[ny][nx] == 0:
                continue

            # 3. 이미 방문한 칸이면 다시 갈 필요 없음
            if visited[ny][nx]:
                continue

            # 4. 다음 칸 터널이 "반대 방향"으로 연결되어 있어야 진짜 이동 가능
            next_type = board[ny][nx]
            if opposite[d] not in tunnel[next_type]:
                continue

            # 이동 가능하면 방문 처리
            visited[ny][nx] = visited[y][x] + 1
            q.append((ny, nx))
            count += 1

    return count


T = int(input())

for tc in range(1, T + 1):
    # N: 세로, M: 가로, R/C: 시작점, L: 제한 시간
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    # 시작 위치에 터널이 없으면 갈 수 있는 곳도 없음
    if board[R][C] == 0:
        print(f"#{tc} 0")
        continue

    answer = bfs(R, C)
    print(f"#{tc} {answer}")