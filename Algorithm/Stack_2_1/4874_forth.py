T = int(input())
for test_case in range(1, 1 + T):

    fort = input().split()
    stack = []
    result = 0
    ok = True

    for i in range(len(fort)):
        token = fort[i]

        if token == '.':
            break

        if token not in '+-/*.':
            stack.append(int(token))

        else:
            if len(stack) < 2:
                ok = False
                break
            a = stack.pop()
            b = stack.pop()

            if token == '+':
                stack.append(b + a)

            elif token == '-':
                stack.append(b - a)

            elif token == '*':
                stack.append(b * a)

            elif token == '/':
                stack.append(b // a)
    if not ok or len(stack) != 1:
                print(f'#{test_case} error')
    else:
        result = stack.pop()
        print(f'#{test_case} {result}')




