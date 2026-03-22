T = int(input())
for test_case in range(1, 1 + T):
    Node, Line = map(int, input().split())
    inf_Line = []

    adj = [[] for _ in range(Node + 1)]

    for _ in range(Line):
        u, v = map(int, input().split())
        adj[u].append(v)

    start, end = map(int, input().split())

    stack = [start]
    visited = set()

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)

        for neighbor in adj[node]:
            if neighbor not in visited:
                stack.append(neighbor)
    print(f'#{test_case} {1 if end in visited else 0}')