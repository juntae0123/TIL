import sys
from collections import deque

sys.stdin = open("input.txt", "r")

# SWEA 5656. 벽돌 깨기
#
# ============================================================
# [문제 해결 후보를 먼저 세워보자]
# ============================================================
#
# 1) 공을 떨어뜨리는 모든 경우를 직접 시뮬레이션하자
#    - 공은 총 N개
#    - 매번 어느 열(column)에 떨어뜨릴지 선택
#    - 열의 개수는 W개
#    - 즉, 경우의 수는 "W^N"
#    - N이 크지 않기 때문에(보통 4 이하) 전부 시도 가능
#
#    => "중복 순열" 형태의 완전탐색 + 시뮬레이션 문제
#
#
# 2) 벽돌이 깨지는 과정은 어떻게 구현할까?
#    - 단순히 한 칸만 0으로 만드는 게 아님
#    - 숫자가 1보다 크면 그 숫자만큼 상하좌우로 연쇄 폭발
#    - 그러므로 "BFS" 또는 "DFS" 로 폭발 범위를 퍼뜨리면 됨
#
#    => 여기서는 큐를 써서 BFS 방식으로 폭발 처리
#
#
# 3) 벽돌이 깨진 뒤에는 어떻게 처리할까?
#    - 빈칸 위에 벽돌이 떠 있게 되므로
#    - 각 열마다 아래로 떨어뜨리는 "중력 처리"가 필요
#
#    => 열 단위로 숫자만 모아서 다시 아래부터 채우기
#
#
# 4) 최종 전략
#    - DFS(재귀)로 "공을 어느 열에 떨어뜨릴지" 전부 탐색
#    - 매 단계마다:
#         1. 현재 열에 공을 떨어뜨리고
#         2. 첫 벽돌을 찾고
#         3. 연쇄 폭발시키고
#         4. 중력 적용하고
#         5. 다음 공으로 재귀
#
# ============================================================
# [시간복잡도 관점]
# ============================================================
#
# 대략 W^N 개 경우를 본다.
# 각 경우마다 폭발 + 중력 시뮬레이션이 들어간다.
# N이 작아서 가능한 전형적인 "완전탐색 + 구현" 문제.
#
# ------------------------------------------------------------
# 방향: 상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def count_bricks(board):
    """현재 보드에 남아 있는 벽돌 개수 세기"""
    cnt = 0
    for y in range(H):
        for x in range(W):
            if board[y][x] != 0:
                cnt += 1
    return cnt


def find_top_brick(board, col):
    """
    col 열에서 가장 위에 있는 벽돌 찾기
    없으면 -1 반환
    """
    for row in range(H):
        if board[row][col] != 0:
            return row
    return -1


def explode(board, sy, sx):
    """
    (sy, sx) 위치의 벽돌부터 연쇄 폭발 처리

    [핵심]
    - 값이 1이면 자기 자신만 깨짐
    - 값이 k면 상하좌우로 (k-1)칸까지 영향
    - 그 범위 안에서 또 숫자>1 벽돌을 만나면 연쇄적으로 계속 터짐

    [왜 BFS?]
    - "터질 벽돌 후보"가 계속 생김
    - 큐에 넣고 순서대로 처리하면 깔끔함
    """
    q = deque()
    q.append((sy, sx, board[sy][sx]))

    # 시작 벽돌도 바로 깨진 것으로 처리
    board[sy][sx] = 0

    while q:
        y, x, power = q.popleft()

        # power가 1이면 자기 자신만 깨지고 끝
        # power가 3이면 1칸, 2칸까지 퍼짐
        for d in range(4):
            for dist in range(1, power):
                ny = y + dy[d] * dist
                nx = x + dx[d] * dist

                # 범위 밖이면 그 방향은 더 볼 필요 없음
                if not (0 <= ny < H and 0 <= nx < W):
                    break

                # 빈칸이면 그냥 지나감
                if board[ny][nx] == 0:
                    continue

                # 벽돌이면 일단 그 숫자를 저장
                next_power = board[ny][nx]

                # 깨졌다고 표시
                board[ny][nx] = 0

                # 숫자가 2 이상이면 연쇄 폭발 후보
                if next_power > 1:
                    q.append((ny, nx, next_power))


def apply_gravity(board):
    """
    벽돌이 깨진 뒤 중력 적용

    [방법 후보]
    1) 빈칸 만날 때마다 위에서 하나씩 끌어내리기
       - 구현은 가능하지만 다소 복잡함

    2) 각 열에서 살아 있는 벽돌만 따로 모은 뒤
       아래에서부터 다시 채우기
       - 훨씬 단순하고 실수 적음

    => 2번 채택
    """
    for x in range(W):
        # 현재 열에서 살아 있는 벽돌만 수집
        temp = []
        for y in range(H):
            if board[y][x] != 0:
                temp.append(board[y][x])

        # 열 초기화
        for y in range(H):
            board[y][x] = 0

        # 아래에서부터 다시 채우기
        idx = H - 1
        for num in reversed(temp):
            board[idx][x] = num
            idx -= 1


def drop_ball(board, col):
    """
    col 열에 공 1개 떨어뜨리기

    [처리 순서]
    1. 해당 열의 가장 위 벽돌 찾기
    2. 벽돌이 없으면 변화 없음
    3. 벽돌이 있으면 연쇄 폭발
    4. 중력 적용
    """
    top = find_top_brick(board, col)

    # 해당 열에 벽돌이 아예 없으면 아무 일도 안 일어남
    if top == -1:
        return

    explode(board, top, col)
    apply_gravity(board)


def dfs(depth, board):
    """
    depth번째 공을 어디에 떨어뜨릴지 결정하는 DFS

    [이 함수의 역할]
    - 공을 총 N번 떨어뜨려야 함
    - 매번 0 ~ W-1 열 중 하나를 선택
    - 모든 선택을 재귀적으로 탐색
    - 남은 벽돌 최소 개수를 갱신

    [가지치기]
    - 이미 남은 벽돌이 0이면 더 볼 필요 없음
    """
    global answer

    # 현재 보드에서 남은 벽돌 수 확인
    remain = count_bricks(board)

    # 이미 하나도 없으면 최적해
    if remain == 0:
        answer = 0
        return

    # 이미 현재 최적해보다 더 좋을 수 없는 경우는 아니지만,
    # depth 종료 시점에서 최소값 비교
    if depth == N:
        answer = min(answer, remain)
        return

    # 가지치기: 이미 답이 0이면 더 탐색할 필요 없음
    if answer == 0:
        return

    # 현재 공을 어느 열에 떨어뜨릴지 모두 시도
    for col in range(W):
        # 원본 보드를 직접 건드리면 안 되므로 깊은 복사
        new_board = [row[:] for row in board]

        # 해당 열에 공 투하
        drop_ball(new_board, col)

        # 다음 공 처리
        dfs(depth + 1, new_board)


T = int(input())
for tc in range(1, T + 1):
    # N: 구슬 개수, W: 가로, H: 세로
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]

    # 최악의 경우 전체 벽돌 수가 답이 될 수 있으므로
    answer = count_bricks(board)

    # DFS 시작
    dfs(0, board)

    print(f"#{tc} {answer}")