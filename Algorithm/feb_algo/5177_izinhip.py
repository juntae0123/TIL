T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (N + 1)
    last = 0

    # 힙에 하나씩 삽입
    for x in arr:
        last += 1
        heap[last] = x

        i = last
        while i > 1:
            p = i // 2
            if heap[p] <= heap[i]:
                break
            heap[p], heap[i] = heap[i], heap[p]
            i = p

    # 마지막 노드의 조상 합
    ans = 0
    i = N // 2
    while i >= 1:
        ans += heap[i]
        i //= 2

    print(f"#{tc} {ans}")