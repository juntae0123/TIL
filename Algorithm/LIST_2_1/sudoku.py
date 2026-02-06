T = int(input())
for test_case in range(1, T + 1):
    sudoku = []
    for _ in range(9):
        sudoku.append(list(map(int, input().split())))
    Is_sudoku = True

    for i in range(9):
        height = set()
        for j in range(9):
            height.add(sudoku[i][j])
        if len(height) != 9:
                Is_sudoku = False

    for i in range(9):
        length = set()
        for j in range(9):
            length.add(sudoku[j][i])
        if len(length) != 9:
                Is_sudoku = False

    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            square = set()
            for i in range(y, y+3):
                for j in range(x, x+3):
                    square.add(sudoku[i][j])
            if len(square) != 9:
                Is_sudoku = False

    print(f'#{test_case} {1 if Is_sudoku else 0}')


