import sys
# 입출력 처리는 이미 구현되어 있습니다
def solve_circuit_wiring(N, K, board, pairs):
    """
    N: 기판의 크기
    K: 단자 쌍의 개수
    board: 2차원 리스트 (0: 빈칸, 1: 장애물)
    pairs: 단자 쌍의 좌표 리스트 [(r1, c1, r2, c2), ...]
    
    Returns: 최소 전선 길이의 합 (불가능할 경우 -1)
    """
    
    min_total_length = float('inf')
    
    # TODO: 휴리스틱, 고립 공간 탐지 등 가지치기 함수들을 설계하십시오.
    
    def dfs(pair_idx, current_length):
        nonlocal min_total_length
        
        # TODO: 백트래킹을 이용한 전선 연결 로직을 구현하십시오.
        pass

    # 탐색 시작
    # dfs(0, 0)
    
    return min_total_length if min_total_length != float('inf') else -1

if __name__ == "__main__":
    
    input_data = sys.stdin.read().split()
    if not input_data:
        exit()
        
    N = int(input_data[0])
    K = int(input_data[1])
    
    idx = 2
    board = []
    for _ in range(N):
        row = []
        for _ in range(N):
            row.append(int(input_data[idx]))
            idx += 1
        board.append(row)
        
    pairs = []
    for _ in range(K):
        r1, c1, r2, c2 = map(int, input_data[idx:idx+4])
        pairs.append((r1, c1, r2, c2))
        idx += 4
        
    result = solve_circuit_wiring(N, K, board, pairs)
    print(result)