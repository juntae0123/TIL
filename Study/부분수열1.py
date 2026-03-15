def dfs(total, start):
    global result

    if total == K:
        result += 1
    
    
    dfs(total,start +1)
    dfs(total + arr[start], start +1)



T = int(input())

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split)())
    result = 0

    dfs(0, 0)

    print(f'#{tc} {result}')