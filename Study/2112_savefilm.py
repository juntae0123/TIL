# 보호 필름 A,B 중 하나의 특성을 가진 셀의 집합 
# 테스트를 통과하려면 같은 행의 K개의 열이 같은 특성이어야함
# 약품을 통해 한 열을 같은 특성의 셀들로 바꿀 수 있다
# 두께 : D, 가로 : W, 합격기준 : K
# A = 0, B = 1
# --------------------설계 -----------------------
'''
새로검색이 핵심 같은 인덱스의 열에 K개만큼 같은 특성을 가진 셀이 있으면 통과
1. for 문으로 아래만 내려가면서 확인 1또는 0을 만남 -> cnt+1 다음 열이 같은 숫자다 -> cnt +1, 다른숫자면 cnt 초기화 후 cnt + 1  cnt = k 가 되면 종료 안되면 실패
   모든 행을 돌려서 모두 true - 성공 case 1
2. false 발생시 약품처리 - 약품cnt + 1 , 처음부터 다시봐야함 >>> 재귀로 약품 처리할건지 안하고 넘어가볼건지 선택? 약품처리하면 첫 x좌표부터 다시 봐야함 
3. 성능검사 통과가 약품처리하지않은 열이라면 안봐도 되긴함
결론 : 재귀로 완전탐색 느낌으로 가면서 각 행의 성능 검사가 통과한 좌표를 저장 - false면 약품 처리를 하고 해당 열이 포함된 통과된곳들도 다시 검사 
      해야할것: dfs(완전 탐색) + 약품 처리 함수 + 성능 검사 함수 + 최소 약품 갯수 갱신(min 으로) + 이것도원래 보드 건들면 안되니 깊은복사
'''
'''필요할줄 알았지만 필요 없어짐
dy = [1]
dx = [0]
'''

def check_row(board):
    # 이 함수는 세로로 내려가면서 K 개만큼 연속된 특성이있는지만 확인하면 됨 전부 되면 1 안되면 -1 반환하자
    if K == 1: # k가 1인 개같은 함정이면 끝내자
        return True
    
    for x in range(W):
        
        idx = 0
        cnt = 1
        passed = False

        while idx < D - 1:

            if board[idx][x] == board[idx + 1][x]:
                cnt += 1

            else:
                cnt = 1
            
            if cnt >= K:
                passed = True
                break

            idx += 1
        if not passed:
            return False

    return True

def drug(board, row, character):

    for x in range(W):
        board[row][x] = character 


def dfs(row, drug_cnt):

    global min_drug

    if drug_cnt >= min_drug:
        return
    
    if row == D:
        if check_row(board):
            min_drug = min(min_drug, drug_cnt)
        return

    # 약품 안넣는 경우
    dfs(row + 1, drug_cnt)

    original = board[row][:]

    # 약품 A
    drug(board, row , 0)
    dfs(row + 1, drug_cnt + 1)

    # 약품 B
    drug(board, row, 1)
    dfs(row + 1, drug_cnt + 1)

    board[row] = original


T = int(input())
for tc in range(1, 1 + T):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    
    # 최악의 경우 K개 행만 바꾸면 무조건 가능
    min_drug = K

    dfs(0, 0)

    print(f'#{tc} {min_drug}')
'''

T = int(input())
for tc in range(1, T + 1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]

    min_drug = K

    # 바로 통과하는 경우 처리
    if K == 1 or check(board):
        min_drug = 0
    else:
        dfs(0, 0)

    print(f'#{tc} {min_drug}')
'''