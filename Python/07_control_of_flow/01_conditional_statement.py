# if문 기본


# 복수 조건문
## 순서 1. 결과: 매우 나쁨
dust = 155

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')


## 순서 2. # 결과: 보통
dust = 155

if dust > 30:
    print('보통')
elif dust > 80:
    print('나쁨')
elif dust > 150:
    print('매우 나쁨')
else:
    print('좋음')


# 중첩 조건문 동작 예시
# 출력: 매우 나쁨
#      위험해요! 나가지 마세요!
dust = 480

if dust > 150:
    print('매우 나쁨')
    if dust > 300:
        print('위험해요! 나가지 마세요!')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:
    print('좋음')

dust =220
if dust > 400:
    print('매우 나쁨')
elif dust > 300:
    print('나쁨')
elif dust > 200:
    print('보통')
    if dust > 250:
        print('이겠냐고;')
    else :
        print('나 김준탠데 이거 맞다')
else :
    print('좋음')