T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    # % -> 0~1
    for i in range(N):
        for j in range(N):
            P[i][j] *= 0.01

    # i번 직원의 일들을 확률 큰 순서로 정렬 (람다 X)
    order = []
    for i in range(N):
        idx_list = list(range(N))
        idx_list.sort(key=P[i].__getitem__, reverse=True)
        order.append(idx_list)

    # 가지치기 상한: 남은 직원들의 "행 최대값" 곱
    row_max = [max(P[i]) for i in range(N)]
    suffix_max = [1.0] * (N + 1)
    for i in range(N - 1, -1, -1):
        suffix_max[i] = suffix_max[i + 1] * row_max[i]

    used = [False] * N
    best = [0.0]   # ✅ nonlocal 대신 리스트로 감싸기

    def dfs(i, cur):
        # 확률은 곱하면 줄어드니까, 현재가 best 이하이면 컷
        if cur <= best[0]:
            return

        # 남은 애들이 각자 최고 확률만 뽑아도 best 못 넘으면 컷
        if cur * suffix_max[i] <= best[0]:
            return

        if i == N:
            best[0] = cur
            return

        for j in order[i]:
            if not used[j]:
                p = P[i][j]
                if p == 0.0:
                    continue
                used[j] = True
                dfs(i + 1, cur * p)
                used[j] = False

    dfs(0, 1.0)
    print(f"#{test_case} {best[0] * 100:.6f}")
