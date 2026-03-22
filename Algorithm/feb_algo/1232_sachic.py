def preorder(v):
    if v == 0:
        return 0
    if left[v] == 0 and right[v] == 0:
        return int(pare[v])

    l = preorder(left[v])
    r = preorder(right[v])

    if pare[v] == '+':
        pare[v] = l + r
        return l + r
    if pare[v] == '-':
        pare[v] = l - r
        return l - r
    if pare[v] == '*':
        pare[v] = l * r
        return l * r
    if pare[v] == '/':
        if r != 0:
            pare[v] = l // r
            return l // r

for tc in range(1, 11):
    N = int(input())

    left = [0] * (N +1)
    right = [0] * (N +1)
    pare = [''] * (N +1)

    for i in range(1, N+1):
        tree = input().split()
        idx = int(tree[0])

        pare[idx] = tree[1]

        if len(tree) == 4:
            left[idx] = int(tree[2])
            right[idx] = int(tree[3])

    ans = preorder(1)
    print(f"#{tc} {ans}")


