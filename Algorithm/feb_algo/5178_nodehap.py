def order(v):
    if v > node:
        return 0

    if tree[v] != 0:
        return tree[v]

    left_sum = order(v * 2)
    right_sum = order(v*2+1)
    tree[v] = left_sum + right_sum
    return tree[v]

T = int(input())
for tc in range(1, T+1):
    node, leaf,  node_num = map(int, input().split())

    tree = [0] * (node + 1)
    for i in range(leaf):
        leaf_num , jungsu = map(int, input().split())
        tree[leaf_num] = jungsu

    order(1)
    print(f"#{tc} {tree[node_num]}")

