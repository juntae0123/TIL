T = 10
for test_case in range(1, 1 + T):
    N = int(input())
    calc = list(input().strip())

    stack = []
    i = 0

    while i < len(calc):
        if calc[i] == '*':
            a = calc[i]
            l = stack.pop()
            r = calc[i+1]
            stack.append(int(l) * int(r))
            i += 2
        else:
            stack.append(calc[i])
            i += 1

    result = int(stack[0])
    i = 1

    while i < len(stack):

        if stack[i]== '+':
            result += int(stack[i + 1])
        i += 2


    print(f'#{test_case} {result}')
