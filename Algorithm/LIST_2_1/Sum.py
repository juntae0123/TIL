for test_case in range(10):
    T = int(input())
    siuu = []
    length_best = 0
    height_best = 0
    Daejung = 0
    Daeyuk = 0
    for _ in range(100):
        siuu.append(list(map(int, input().split())))
    for i in range(100):
        length = 0
        for j in range(100):
            length += siuu[i][j]
        if length_best < length:
            length_best = length
    for i in range(100):
        height = 0
        for j in range(100):
            height += siuu[j][i]
        if height_best < height:
            height_best = height
    for i in range(100):
        Daejung += siuu[i][i]

    for i in range(100):
        Daeyuk += siuu[100-i-1][i]
    Dae = max(Daeyuk, Daejung)
    best = max(Dae, length_best, height_best)
    print(f'#{T} {best}')
