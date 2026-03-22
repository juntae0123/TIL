T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    # (피자번호, 치즈)
    q = []

    next_idx = 0  # 아직 오븐에 안 들어간 다음 피자 index (0-based)

    # 처음 N개 투입
    for _ in range(N):
        q.append((next_idx + 1, cheese[next_idx]))
        next_idx += 1

    # 오븐 시뮬레이션
    while len(q) > 1:
        num, c = q.pop(0)
        c //= 2

        if c > 0:
            q.append((num, c))
        else:
            if next_idx < M:
                q.append((next_idx + 1, cheese[next_idx]))
                next_idx += 1

    print(f"#{test_case} {q[0][0]}")
'''
from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    q = deque()
    next_idx = 0  # 아직 안 들어간 다음 피자 인덱스

    # 처음 N개 오븐에 넣기
    for _ in range(N):
        q.append((next_idx + 1, cheese[next_idx]))
        next_idx += 1

    # 오븐 돌리기
    while len(q) > 1:
        num, c = q.popleft()   # 맨 앞 피자 꺼냄
        c //= 2                # 치즈 반으로

        if c > 0:
            q.append((num, c))  # 다시 뒤에 넣기
        else:
            if next_idx < M:    # 아직 안 넣은 피자 있으면
                q.append((next_idx + 1, cheese[next_idx]))
                next_idx += 1

    print(f"#{test_case} {q[0][0]}")

'''