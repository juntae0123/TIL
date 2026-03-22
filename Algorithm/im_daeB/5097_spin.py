from collections import deque

T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())

    spin = deque(map(int, input().split()))


    for i in range(M):
        k = i % N
        spin.append(spin.popleft())
    
    print(f'#{test_case} {spin[0]}')


