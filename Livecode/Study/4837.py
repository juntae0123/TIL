def dfs(cnt, total, start):
    global result

    if total > K:
        return
    
    if cnt > N:
        return
    
    if start == 12:
        if cnt == N and total == K:
            result += 1
        return 
        
    dfs(cnt, total, start + 1)
    dfs(cnt + 1, total + arr[start], start + 1)


T = int(input())
for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    arr = [i for i in range(1,13)]
    result = 0

    dfs(0, 0, 0)

    print(f'#{tc} {result}')