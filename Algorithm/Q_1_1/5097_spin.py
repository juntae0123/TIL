from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = deque(map(int, input().split()))

    M %= N   # 쓸데없는 회전 제거

    for _ in range(M):
        arr.append(arr.popleft())

    print(f"#{test_case} {arr[0]}")
