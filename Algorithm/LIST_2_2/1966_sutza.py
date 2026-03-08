''' 선택 정렬
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Nparty = list(map(int, input().split()))
    for i in range(N):
        min_Nparty = i
        for j in range(i+1, N):
            if Nparty[j] < Nparty[min_Nparty]:
                min_Nparty = j
        Nparty[i], Nparty[min_Nparty] = Nparty[min_Nparty], Nparty[i]

    print(f'#{test_case}', *Nparty)
    바로 교환하는 선택 정렬
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Nparty = list(map(int, input().split()))
    for i in range(N):
        for j in range(i+1, N):
            if Nparty[i] > Nparty[j]:
                Nparty[i], Nparty[j] = Nparty[j], Nparty[i]
    print(f'#{test_case}', *Nparty)
'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    Nparty = list(map(int, input().split()))
    for i in range(N - 1):
        swapped = False
        for j in range(N - 1 - i):
            if Nparty[j] > Nparty[j + 1]:
                Nparty[j], Nparty[j + 1] = Nparty[j + 1], Nparty[j]
        if not swapped:
            break
    print(f'#{test_case}', *Nparty)