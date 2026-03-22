T = int(input())
for test_case in range(1, T + 1):
    max_move, last_stop, charge_count = map(int, input().split())

    # 충전소 표시
    has_charge = [0] * (last_stop + 1)
    charge_positions = list(map(int, input().split()))
    for pos in charge_positions:
        has_charge[pos] = 1

    current_stop = 0
    charge_used = 0

    # 한 번에 종점 못 갈 때만 반복
    while current_stop + max_move < last_stop:
        next_stop = current_stop + max_move  # 최대로 갈 수 있는 위치

        # 뒤로 오면서 가장 먼 충전소 찾기
        while next_stop > current_stop and has_charge[next_stop] == 0:
            next_stop -= 1

        # 충전소 못 찾으면 실패
        if next_stop == current_stop:
            charge_used = 0
            break

        # 충전
        charge_used += 1
        current_stop = next_stop

    print(f'#{test_case} {charge_used}')
