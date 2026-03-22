T = int(input())
for test_case in range(1, 1 + T):
    N = int(input())
    min_lis = [list(map(int, input().split())) for _ in range(N)]

    min_result = 9999999
    stack =[(0,0,0)]


    while stack:
        i, used_mask, result= stack.pop()

        if result >= min_result:
            continue
        if i == N:
            if result < min_result:
                min_result = result
            continue

        for x in range(N):
            if (used_mask & (1 << x)) == 0:
                stack.append((i + 1, used_mask | (1 << x), result + min_lis[i][x]))
    print(f'#{test_case} {min_result}')


'''
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    min_lis = [list(map(int, input().split())) for _ in range(N)]

    min_result = float('inf')

    # (현재 행 i, 사용한 열 set, 누적합)
    stack = [(0, set(), 0)]

    while stack:
        i, visited_x, result = stack.pop()

        # 가지치기
        if result >= min_result:
            continue

        # 끝까지 왔으면 최소 갱신
        if i == N:
            min_result = result
            continue

        # i번째 행에서 열 선택
        for x in range(N):
            if x not in visited_x:
                new_set = visited_x.copy()   # 중요
                new_set.add(x)
                stack.append(
                    (i + 1, new_set, result + min_lis[i][x])
                )

    print(f'#{test_case} {min_result}')
'''

