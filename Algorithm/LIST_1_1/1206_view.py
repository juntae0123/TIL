T = 10
for test_case in range(1, T+1):
    building = int(input())
    height = list(map(int, input().split()))
    sum_height = 0
    # 양옆 2칸씩의 맥스값을 찾아서 빼주면 된다
    for i in range(2, building-2):
        key = max(height[i-1], height[i-2], height[i+1], height[i+2])
        if height[i] > key:
            sum_height += (height[i]-key)
    print(f'#{test_case} {sum_height}')


'''윤씨 풀이
T = 10
for tc in range(1,T+1):
    building = int(input())
    height = list(map(int,input().split()))
    diff =[]
    for i in range(2,building-2):
        if height[i]< height[i-1] or height[i]< height[i+1] or height[i]< height[i-2] or height[i]< height[i+2]:
            pass
        else:
            tmp =[height[i]- height[i-1],height[i]- height[i-2],height[i]- height[i+1],height[i]- height[i+2]]
            diff.append(min(tmp))
 
    print(f'#{tc} {sum(diff)}')
'''
