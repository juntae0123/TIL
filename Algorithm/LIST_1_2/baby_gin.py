
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
T = int(input())
for test_case in range(1, T + 1):
    cnt = [0]*10
    N = list(map(int, input().strip()))
    for an in N:
        cnt[an] += 1
    runn = 0
    triplet = 0
    i = 0

    while i < 9:
        if cnt[i] >= 3:
            cnt[i] -= 3
            triplet += 1
            continue
        if i<=7 and cnt[i] >= 1 and cnt[i+1] >= 1 and cnt[i +2] >=1:
            cnt[i] -= 1
            cnt[i+1] -= 1
            cnt[i+2] -= 1
            runn += 1
            continue
        i += 1
    print(f'#{test_case} {1 if runn + triplet == 2 else 0}')


