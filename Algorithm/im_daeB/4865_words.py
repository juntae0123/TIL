T = int(input())
for test_case in range(1, 1 + T):
    key = list(input())
    quest = list(input())
    
    maxcnt = 0
    for i in range(len(key)):
        cnt = 0
        for j in range(len(quest)):
            if key[i] == quest[j]:
                cnt += 1

        if cnt >= maxcnt:
            maxcnt = cnt
    print(f'#{test_case} {maxcnt}')
    