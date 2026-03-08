T = int(input())
for test_case in range(1, T + 1):
    P, Astu, Bstu = list(map(int, input().split()))

    count = [0, 0]
    who =[Astu, Bstu]

    for i in range(2):
        l, r = 1, P
        c = (l + P) // 2
        while c != who[i]:
            count[i] += 1
            if who[i] < c:
                r = c
            if who[i] > c:
                l = c
            c = (l + r) // 2
    if count[0] < count[1]:
        print(f'#{test_case} A')
    if count[0] > count[1]:
        print(f'#{test_case} B')
    if count[0] == count[1]:
        print(f'#{test_case} 0')
