'''T = int(input())

for test_case in range(1, T+1):
    iron = input()
    iron_list = list(iron.strip())
    razor = [0] * len(iron_list)
    countp = 0
    countR = 0
    for i in range(len(iron_list)):
        if iron_list[i] == '(':
            countp += 1
        else:
            countp -= 1
            if iron_list[i-1] == '(':
                countR += countp
            else:
                countR += 1

    print(f'#{test_case} {countR}')
'''
case_count = int(input())

for case_idx in range(1, case_count + 1):
    bracket_str = input().strip()
    bracket_list = list(bracket_str)

    # 레이저 위치 표시
    laser_flag = [0] * len(bracket_list)

    for pos in range(len(bracket_list) - 1):
        if bracket_list[pos] == '(' and bracket_list[pos + 1] == ')':
            laser_flag[pos] = 1
            laser_flag[pos + 1] = 1

    open_bar_count = 0 #조각ㄱ 카운트
    piece_count = 0 # 결과 받을 카운트

    for pos in range(len(bracket_list)):
        if bracket_list[pos] == '(':
            if laser_flag[pos] == 0:      # 레이저 '(' 아님
                open_bar_count += 1
        else:  # ')'
            if laser_flag[pos] == 1:      # 레이저 ')'
                piece_count += open_bar_count
            else:                          # 막대 끝
                open_bar_count -= 1
                piece_count += 1

    print(f'#{case_idx} {piece_count}')