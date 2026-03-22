T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    card = list(map(int, input().strip()))
    cnt = [0] * 10

    for num in card:
        cnt[num] += 1
    
    k = 0
    max_cnt = 0   
    
    for i in range(10):
      
        if cnt[i] >= max_cnt:
            max_cnt = cnt[i]
            k = i
    print(f'#{test_case} {k} {max_cnt}')