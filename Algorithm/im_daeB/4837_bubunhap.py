T = int(input())
for test_case in range(1, 1 + T):
    N, K = map(int, input().split())
    
    bubun = list(range(1, 13))
    
    sum = 0
    
    for i in range(1 << 12):
        m_sum = 0
        m_count = 0

        for j in range(12):
            if i & (1 << j):
                m_sum += bubun[j]
                m_count += 1
        if m_count == N and m_sum == K:
            sum += 1
    print(f'#{test_case} {sum}')





'''
    arr = [1,2,3,4,5]
    sum = 0
    for i in range(1 << 5):
        m_sum = 0 
        m_cnt = 0
        for j in range(5):
            if i & (1 << j):
                m_sum += arr[j]
                m_cnt += 1
        if m_sum == 9 and m_cnt == 3:
            sum += 1
'''