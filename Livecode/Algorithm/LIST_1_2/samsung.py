T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    diff = [0] * 5002
    for _ in range(N):
        A, B = map(int, input().split())
        diff[A] += 1
        diff[B+1] -= 1

    cnt = [0] * 5001
    running = 0
    for stop in range(1, 5001):
        running += diff[stop]
        cnt[stop] = running
    P = int(input())
    ans = []
    for _ in range(P):
        J = int(input())
        ans.append(str(cnt[J]))
        print(f"#{test_case} " + " ".join(ans))
