for test_case in range(10):
    T, N = map(int, input().split())
    data = list(map(int, input().split()))

    gan = [[] for _ in range(100)]


    for i in range(0, 2*N, 2):
        a = data[i]
        b = data[i+1]

        gan[a].append(b)

    visited = [0] * 100
    visited[0] = 1
    stack = [0]

    while stack:
        x = stack.pop()


        if x == 99:
            break

        for nv in gan[x]:
            if visited[nv] == 0:
                stack.append(nv)
                visited[nv] = 1




    ans = 1 if visited[99] == 1 else 0
    print(f'#{T} {ans}')