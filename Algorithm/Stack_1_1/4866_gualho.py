T = int(input())
for test_case in range(1, T + 1):
    line = input()
    stack = []
    valid = True

    pair = {')': '(', '}': '{'}

    for ch in line:
        if ch in '({':
            stack.append(ch)
        elif ch in ')}':
            if not stack:
                valid = False
                break
            if stack[-1] != pair[ch]:
                valid = False
                break
            stack.pop()

    if stack:
        valid = False

    print(f'#{test_case} {1 if valid else 0}')