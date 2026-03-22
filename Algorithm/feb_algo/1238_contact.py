from collections import deque
for tc in range(1, 11):
    N, start = map(int, input().split())

    data = list(map(int, input().split()))
    path = [[] for _ in range(101)]
    for a in range(0, N, 2):
        x = data[a]
        y = data[a+1]

        path[x].append(y)

    q = deque([start])
    visited = [-1] * 101
    visited[start] = 0
    while q:
        x = q.popleft()

        for near in path[x]:
            if visited[near] == -1:
                visited[near] = visited[x] + 1
                q.append(near)

    max_path = max(visited)
    king = 0

    for i in range(len(visited)):
        if visited[i] == max_path:
            king = i

    print(f'#{tc} {king}')
''' 왜안됨? ㅋㅋ
for tc in range(1, 11):
    N, start = map(int, input().split())

    data = list(map(int, input().split()))
    path = [[] for _ in range(101)]

    for a in range(0, N, 2):
        x = data[a]
        y = data[a + 1]
        path[x].append(y)

    stack = [(start, 0)]
    visited = [-1] * 101
    visited[start] = 0

    while stack:
        x, d = stack.pop()

        for near in path[x]:
            nd = d + 1
            if visited[near] < nd:
                visited[near] = nd
                stack.append((near, nd))

    max_path = max(visited)
    king = 0

    for i in range(len(visited)):
        if visited[i] == max_path:
            king = i

    print(f'#{tc} {king}')
'''




