T = 10
for tc in range(1, T + 1):
    N = int(input())
    h = list(map(int, input().split()))

    view = 0
    for i in range(2, N - 2):
        neighbor_max = max(h[i-2], h[i-1], h[i+1], h[i+2])
        if h[i] > neighbor_max:
            view += h[i] - neighbor_max

    print(f'#{tc} {view}')
