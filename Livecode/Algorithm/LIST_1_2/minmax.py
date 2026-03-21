T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    yang = int(input())
    lis = list(map(int, input().split()))
    max_lis = max(lis)
    min_lis = min(lis)
    max_cnt = 0
    min_cnt = 0
    min_found = False
    for i in range(yang):
        if lis[i] == max_lis:
            max_cnt = i
        if lis[i] == min_lis and not min_found:
            min_cnt = i
            min_found = True
    result = abs(max_cnt - min_cnt)
    print(f'#{test_case} {result}')

