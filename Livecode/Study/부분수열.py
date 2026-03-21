def dfs(total,start):
    global result

    if total == S:
        result += 1
 
    
    for i in range(start, N):
        dfs(total + arr[i], i + 1)

N, S=map(int,input().split())
arr = list(map(int,input().split()))

result = 0
dfs(0,0)
if S == 0:
    result -= 1
print(result)
'''
def dfs(cnt,total,start):# cnt 필요없어 result가 cnt 잖아
    global result

    if cnt == N: #### cnt 가 필요없이 for문 다돌면 끝나서 필요없음 마찬가지로
        return

    if total == S:
        result += 1
        return # 이거 있으면 total == S 한번 만족하면 끝나버림
    
    for i in range(start, N):
        dfs(cnt + 1, total +arr[i], i + 1)

N, S=map(int,input().split())
arr = list(map(int,input().split()))
result = 0
dfs(0,0,0)
if S == 0:
    result -= 1
print(result)
'''

def dfs(total, start):
    global result

    if total == S:
        result += 1
    

    for i in range(start, N):
        dfs(total + arr[i], i + 1)
    
N, S = map(int, input().split())
arr = list(map(int, input().split()))


result = 0
dfs(0, 0)
if S == 0:
    result -= 1

print(result)