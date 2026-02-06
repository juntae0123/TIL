T = int(input())
for test_case in range(1, 1+T):
    seok = []
    len_seok = 0

    for i in range(5):
        a = input().strip()
        seok.append(a)
        if len(a) > len_seok:
            len_seok = len(a)

    eui = [[''] * len_seok for _ in range(5)]

    for j in range(len_seok):
        for i in range(5):
            if j < len(seok[i]):
                eui[i][j] = seok[i][j]
    ans = []
    for j in range(len_seok):
        for i in range(5):
            if eui[i][j] != '':
                ans.append(eui[i][j])
    print(f'#{test_case} {"".join(ans)}')
