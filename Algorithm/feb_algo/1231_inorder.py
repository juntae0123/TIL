def inorder(v):
    if v == 0:
        return

    inorder(left[v])
    result.append(val[v])
    inorder(right[v])

for tc in range(1, 11):
    N = int(input())
    val = [''] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for i in range(N):
        info = input().split()
        idx = int(info[0])
        val[idx] = info[1]
        if len(info) >= 3:
            left[idx] = int(info[2])
        if len(info) >= 4:
            right[idx] = int(info[3])

    result = []
    inorder(1)
    print(f"#{tc} {''.join(result)}")



