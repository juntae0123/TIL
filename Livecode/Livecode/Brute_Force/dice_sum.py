path = []
result = 0

def dice(cnt):
    global result

    if cnt == 3:
        if sum(path) <= 10:
            print(*path)
            result += 1            
        return
    
    for num in range(1, 7):
        path.append(num)
        dice(num+1)
        path.pop()

dice(0)
'''---------------------업그레이드--------------'''


path = []
result = 0

def dice(cnt, total):
    global result
    if total > 10:
        return

    if cnt == 3:
        if total <= 10:
            print(*path)
            result += 1            
        return
    
    for num in range(1, 7):
        path.append(num)
        dice(num+1,total + num)
        path.pop()

dice(0)