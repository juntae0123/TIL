T = int(input())
for test_case in range(1, 1 + T):
    N = 5
    arr = []
    maxlen = 0

    for i in range(N):
        s = input().strip()
        arr.append(list(s))
        if len(s) >= maxlen:
            maxlen = len(s)

    result = []
    for c in range(maxlen):      
        for r in range(N):       
            if c < len(arr[r]):  
                result.append(arr[r][c])

    print(f"#{test_case} {''.join(result)}")
            