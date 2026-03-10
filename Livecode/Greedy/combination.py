# 5명중 N명을 뽑을 것이다
arr = ['A', 'B', 'C', 'D', 'E']
N = 3
path = []

# N 명을 뽑는다 -> depth : N
# 5 명 중 하나를 선택 -> branch : 5
# 전체 순열코드 부터 시작
# 직전 선택을 다음 재귀 호출로 넘겨주고
# 그 다음부터 선택하도록 구성

def recur(cnt, prev):
    if cnt == N:
        return
    # 이전에 선택했던것 다음부터 탐색하자
    for i in range(prev, len(arr)):
        path.append(arr[i])
        recur(cnt + 1, i) # 이전 선택을 함께 전달
        path.pop()

recur(0)