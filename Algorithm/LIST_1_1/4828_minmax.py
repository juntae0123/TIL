T = int(input())
for test_case in range(1, T+1):
    jung = int(input())
    yang = list(map(int, input().split()))
    mima = sorted(yang)
    result = abs(mima[jung -1] - mima[0])
    print(f'#{test_case} {result}')