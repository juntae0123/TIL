T = 10
for test_case in range(1, 1 + T):
    N = int(input())
    gual = input()
    pair = {
        '}': '{',
        ']': '[',
        ')': '(',
        '>': '<'
    }

    stack = []

    is_ok = True

    for ch in gual:
        if ch in '{[(<':
            stack.append(ch)
        elif ch in '}])>':
            if stack and pair[ch] == stack[-1]:
                stack.pop()
            else:
                is_ok = False
                break

    if stack:
        is_ok = False

    print(f'#{test_case} {1 if is_ok  else 0}')


