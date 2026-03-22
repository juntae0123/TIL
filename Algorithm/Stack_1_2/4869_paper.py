T = int(input())

def fire(N):
    if N == 1:
        return 1
    if N == 2:
        return 3
    dp = [0] * (N+1)
    dp[1] = 1
    dp[2] = 3
    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + 2 * dp[i - 2]
    return dp[N]


for test_case in range(1, 1 + T):
    paper = int(input()) // 10

    result = fire(paper)

    print(f'#{test_case} {result}')
