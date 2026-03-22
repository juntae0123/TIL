T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    tor = list(map(int, input().split()))

    def rsp(p1, p2):
        n1, a = p1
        n2, b = p2

        if a == b:
            return p1  # 비기면 왼쪽(앞사람)
        elif (a == 1 and b == 3) or (a == 2 and b == 1) or (a == 3 and b == 2):
            return p1
        else:
            return p2

    def solve(l, r):
        if l == r:
            return (l + 1, tor[l])   # (번호, 카드)
        mid = (l + r) // 2
        left = solve(l, mid)
        right = solve(mid + 1, r)
        return rsp(left, right)

    ans = solve(0, N - 1)
    print(f'#{test_case} {ans[0]}')