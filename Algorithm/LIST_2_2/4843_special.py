def popp(a):
    if a:
        return a.pop()
    return None

def popb(a):
    if a:
        return a.pop(0)
    return None


T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    spec = sorted(list(map(int, input().split())))
    soor =[]

    for _ in range(int(N/2)):
        soor.append(popp(spec))
        soor.append(popb(spec))
    if spec:
        soor.append(popp(spec))

    print(f'#{test_case}', *soor[:10])

