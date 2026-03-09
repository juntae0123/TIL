# map 함수 사용 기본
numbers = [1, 2, 3]
result = map(str, numbers)

print(result)  # <map object at 0x00000239C915D760>
print(list(result))  # ['1', '2', '3']


# map 함수 활용 1 - input과 함께 사용
# 터미널 창에서 1 2 3 입력 (공백 주의)
numbers1 = input().split()
print(numbers1)  # ['1', '2', '3']

## 터미널 창에서 1 2 3 입력 (공백 주의)
numbers2 = list(map(int, input().split()))
print(numbers2)  # [1, 2, 3]


# map 함수 활용 2 - lambda와 함께 사용
numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


# lambda 미사용
squared1 = list(map(square, numbers))
print(squared1)  # [1, 4, 9, 16, 25]

# lambda 사용
squared2 = list(map(lambda x: x**2, numbers))
print(squared2)  # [1, 4, 9, 16, 25]
