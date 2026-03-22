T = int(input())
for test_case in range(1, 1+T):
    N, M = list(map(int, input().split()))
    sui = []

    for _ in range(N):
        sui.append(input().strip())
    is_suishi = False
