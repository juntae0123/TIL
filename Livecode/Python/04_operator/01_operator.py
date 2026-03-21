# 복합 연산자
y = 10
y -= 4
# y = y - 4
print(y)  # 6

z = 7
z *= 2
print(z)  # 14

w = 15
w /= 4
print(w)  # 3.75

q = 20
q //= 3
print(q)  # 6


# 비교 연산자
print(3 > 6)  # False

# == 연산자
print(2 == 2.0)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False
print(1 == True)  # True

# is 비교 연산자
# SyntaxWarning: "is" with a literal. Did you mean "=="?
print(1 is True)  # False
print(2 is 2.0)  # False

# 왜 is 대신 ==를 사용해야 하나?
# 1(정수)과 True(불리언)는 다른 객체이다.
print(1 is True)  # False
# 1과 True의 '값'은 논리적으로 같다.
print(1 == True)  # True

# 2(정수)와 2.0(실수)은 다른 객체이다.
print(2 is 2.0)  # False
# 2와 2.0의 '값'은 논리적으로 같다.
print(2 == 2.0)  # True

# is 연산자는 언제 사용하는가?
# 싱글턴 객체 비교할 때
x = None
# 권장
if x is None:
    print('x는 None입니다.')
# 비권장
if x == None:
    print('x는 None입니다.')


x = True
y = True
print(x is y)  # True
print(True is True)  # True
print(False is False)  # True
print(None is None)  # True


# 논리 연산자
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print(not 0)  # True


# 논리 연산자 & 비교 연산자
num = 15
result = (num > 10) and (num % 2 == 0)
print(result)  # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result)  # True
