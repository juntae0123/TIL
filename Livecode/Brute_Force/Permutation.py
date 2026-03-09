path = []

def recur(cnt):
    if cnt == 2:
        print(path)
        return

    for i in range(3):
        if i in path: # in 시간복잡도 : O(N) 쓰지마라
            continue

        path.append(i)
        recur(cnt + 1)
        path.pop()

recur(0)


N = 7
path = []
used = [0] * N  # N개의 종류가 있을 경우 N개 만큼 만든다.


def recur2(cnt):
    if cnt == 2:
        print(*path)
        return

    for i in range(1,7):
       
        if used[i]: # 이미  i 를 사용했다면 
            continue

        used[i] = 1  # 방문 처리
        path.append(i)
        recur2(cnt + 1)
        path.pop()
        used[i] = 0

recur2(0)