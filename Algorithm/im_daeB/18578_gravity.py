T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    height = list(map(int, input().split()))
    max_height = 0

    for i in range(N):

        if N - i - 1 <= max_height:
            break

        count = 0
        j = i + 1
        while j < N:
            if count + (N - j) <= max_height:
                break

            if height[i] > height[j]:
                count += 1

            j += 1

        max_height = max(max_height, count)  

    print(f'#{test_case} {max_height}')
