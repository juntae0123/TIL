from collections import deque

T = int(input())
for test_case in range(1, 1 + T):
    node, line = map(int, input().split())

    arr = [[] for _ in range(node + 1)]

    for _ in range(line):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)         

    start, end = map(int, input().split())

    d = deque([start])
    visited = [0] * (node + 1)
    visited[start] = 1            

    while d:
        x = d.popleft()

        if x == end:
            break

        for nx in arr[x]:
            if visited[nx] == 0:
                visited[nx] = visited[x] + 1
                d.append(nx)


    ans = 0 if visited[end] == 0 else visited[end] - 1
    print(f'#{test_case} {ans}')
