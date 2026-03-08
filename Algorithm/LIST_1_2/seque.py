T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    su = int(input())
    ze_one = list(map(int, input().strip()))
    yeah = 1
    cnt = [0] * su
    a = 0
    for i in range(0, su):
        if ze_one[i-1] == ze_one[i] and ze_one[i] == 1:
            cnt[a] += 1
        if ze_one[i-1] != ze_one[i] and ze_one[i] == 1:
            if a < su -1:
                a += 1
                cnt[a] += 1
    print(f'#{test_case} {max(cnt)}')

