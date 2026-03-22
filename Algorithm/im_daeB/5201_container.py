T = int(input())
for test_case in range(1, 1 + T):
    N, M = map(int, input().split())
    N_weight =sorted(list(map(int, input().split())), reverse=True)
    M_volume =sorted(list(map(int, input().split())), reverse=True)
    weight = 0
    j = 0

    for i in range(M):
        while j < N and N_weight[j] > M_volume[i]:
            j += 1 
            
        if j < N:   
            weight += N_weight[j]
            j += 1  

    
    print(f'#{test_case} {weight}')

                    
