T = int(input())
for tc in range(1, T + 1):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))

    V = max(data)
    path = [[] for _ in range(V + 1)]

    for i in range(0, 2 * E, 2):
        p = data[i]
        c = data[i + 1]
        path[p].append(c)

    cnt = 0
    stack = [N]

    while stack:
        x = stack.pop()
        cnt += 1

        for child in path[x]:
            stack.append(child)

    print(f"#{tc} {cnt}")