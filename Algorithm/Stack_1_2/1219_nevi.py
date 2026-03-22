T = 10
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    nev = list(map(int, input().split()))
    nev_d = {}
    for i in range(len(nev)):
        if i % 2 == 0:
            nev_d.setdefault(nev[i], [])

        if i % 2 == 1:
            nev_d.setdefault(nev[i - 1], []).append(nev[i])
    start = 0
    end = 99
    stack = [start]
    visited = set()
    while stack:
        node = stack.pop()

        if node in visited:
            continue
        visited.add(node)

        for neighbor in nev_d.get(node, []):
            if neighbor not in visited:
                stack.append(neighbor)

    print(f'#{test_case} {1 if end in visited else 0}')

