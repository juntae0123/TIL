T = int(input())
for test_case in range(1, T + 1):
    length = int(input())
    sut = sorted(list(map(int, input().split())))
    print(f'#{test_case}', *sut)



