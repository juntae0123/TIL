T = int(input())

for tc in range(1, T + 1):
    rect_cnt = int(input())
    rects = [list(map(int, input().split())) for _ in range(rect_cnt)]

    # 서로 다른 색 사각형 쌍의 "교집합 직사각형"들을 모음 (half-open: [x1,x2)×[y1,y2))
    inter_rects = []
    n = len(rects)

    for i in range(n):
        for j in range(i + 1, n):
            # 색이 같으면 보라색 교집합 대상이 아님
            if rects[i][4] == rects[j][4]:
                continue

            ax1, ay1, ax2, ay2 = rects[i][0], rects[i][1], rects[i][2], rects[i][3]
            bx1, by1, bx2, by2 = rects[j][0], rects[j][1], rects[j][2], rects[j][3]

            # 좌표 정규화 (뒤집혀 들어와도 안전)
            ax1, ax2 = sorted((ax1, ax2))
            ay1, ay2 = sorted((ay1, ay2))
            bx1, bx2 = sorted((bx1, bx2))
            by1, by2 = sorted((by1, by2))

            # 끝점 포함이라 half-open으로 변환 (x2+1, y2+1)
            ax2 += 1
            ay2 += 1
            bx2 += 1
            by2 += 1

            # 교집합: 시작은 max, 끝은 min
            ix1 = max(ax1, bx1)
            iy1 = max(ay1, by1)
            ix2 = min(ax2, bx2)
            iy2 = min(ay2, by2)

            # 실제 면적이 있으면 저장
            if ix1 < ix2 and iy1 < iy2:
                inter_rects.append((ix1, iy1, ix2, iy2))

    # 교집합이 없다면 보라색 면적(칸 수) = 0
    if not inter_rects:
        print(f'#{tc} 0')
        continue

    # 좌표 압축을 위한 좌표 수집
    x_coords = set()
    y_coords = set()
    for x1, y1, x2, y2 in inter_rects:
        x_coords.add(x1)
        x_coords.add(x2)
        y_coords.add(y1)
        y_coords.add(y2)

    x_coords = sorted(x_coords)
    y_coords = sorted(y_coords)

    # 좌표 -> 인덱스
    x_to_i = {x: i for i, x in enumerate(x_coords)}
    y_to_i = {y: i for i, y in enumerate(y_coords)}

    # 압축 격자에 칠하기 (합집합)
    covered = [[False] * (len(y_coords) - 1) for _ in range(len(x_coords) - 1)]

    for x1, y1, x2, y2 in inter_rects:
        xi1 = x_to_i[x1]
        xi2 = x_to_i[x2]
        yi1 = y_to_i[y1]
        yi2 = y_to_i[y2]

        for xi in range(xi1, xi2):
            for yi in range(yi1, yi2):
                covered[xi][yi] = True

    # 합집합 면적(=보라색 칸 수) 계산
    purple_cells = 0
    for xi in range(len(x_coords) - 1):
        dx = x_coords[xi + 1] - x_coords[xi]
        for yi in range(len(y_coords) - 1):
            if covered[xi][yi]:
                dy = y_coords[yi + 1] - y_coords[yi]
                purple_cells += dx * dy

    print(f'#{tc} {purple_cells}')
"""
T = int(input())

for tc in range(1, T + 1):
    rect_cnt = int(input())

    # 4836은 좌표가 0~9인 10x10 격자
    grid = [[0] * 10 for _ in range(10)]

    for _ in range(rect_cnt):
        x1, y1, x2, y2, color = map(int, input().split())

        # 문제는 "끝점 포함"이라 +1 해줘야 함
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 1   # 칠해진 횟수 누적

    purple = 0
    for x in range(10):
        for y in range(10):
            if grid[x][y] >= 2:   # 2번 이상 칠해졌으면 보라색
                purple += 1

    print(f'#{tc} {purple}')
"""