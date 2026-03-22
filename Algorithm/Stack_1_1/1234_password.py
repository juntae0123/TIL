T = 10
for test_case in range(1, 1 + T):
    N, M = input().split()
    N = int(N)

    stack = []

    for ch in M:
        if stack and stack[-1] == ch :
            stack.pop()
        else:
            stack.append(ch)
    print(f'#{test_case} {"".join(stack)}')