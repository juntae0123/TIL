T = int(input())
for test_case in range(1, T +1):
    N, M = list(map(int, input().split()))
    puzzle = []

    answer = 0
    for _ in range(N):
        puzzle.append(list(map(int, input().split())))

    puzzle_list = [[0] * N for _ in range(1)]
    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                count += 1
            else:
                if count == M:
                    answer += 1
                count = 0
        if count == M:
            answer += 1

    for i in range(N):
        count = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                count += 1
            else:
                if count == M:
                    answer += 1
                count = 0
        if count == M:
            answer += 1

    print(f'#{test_case} {answer}')
