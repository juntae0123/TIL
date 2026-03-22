T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())

    def trian(num):
        if num == 1:
            return [[1]]
        pasca = []

        for i in range(1, num + 1):
            pasca.append([1] * i)

        for i in range(1, num):
            for j in range(1, i):
                pasca[i][j] = pasca[i - 1][j - 1] + pasca[i - 1][j]
        return pasca
    print(f'#{test_case}')
    pas = trian(N)

    for row in pas:
        print(*row)
