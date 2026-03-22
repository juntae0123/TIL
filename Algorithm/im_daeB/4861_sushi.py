T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    sushi = [list(input().strip()) for _ in range(N)]

    ans = ""

    for i in range(N):
        for start in range(N - M + 1):
            word = sushi[i][start:start+M]
            ok = True
            for j in range(M // 2):
                if word[j] != word[-1-j]:
                    ok = False
                    break
            if ok:
                ans = ''.join(word)
                break
        if ans:
            break

    if not ans:
        for i in range(N):
            for start in range(N - M + 1):
                word = [sushi[start+k][i] for k in range(M)]
                ok = True
                for j in range(M // 2):
                    if word[j] != word[-1-j]:
                        ok = False
                        break
                if ok:
                    ans = ''.join(word)
                    break
            if ans:
                break

    print(f'#{test_case} {ans}')
