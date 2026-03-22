T = 10
for test_case in range(1, 1 + T):
    N = int(input())
    infix = input().strip()

    stack = []
    postfix = []

    for st in infix:
        if st.isdigit():
            postfix.append(st)
        else:
            while stack:
                postfix.append(stack.pop())
            stack.append(st)

    while stack:
        postfix.append(stack.pop())

    calc = []
    for token in postfix:
        if token.isdigit():
            calc.append(int(token))
        else:
            b = calc.pop()
            a = calc.pop()
            calc.append(a + b)
    print(f'#{test_case} {calc[0]}')