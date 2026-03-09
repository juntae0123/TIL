# 함수 정의
def make_sum(x, y):
    """
    이것은 두 수를 파라미터로 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    
    :param x: Description
    :param y: Description
    """
    result = x + y
    return result

# 함수 호출 및 반환 값 할당
# result = make_sum(100, 200)
# print(result)


# [번외] print() 함수는 반환값이 없다.
# result2 = print(100)
# print(result2)  # None


def my_func():
    """
    Docstring for my_func
    이 함수는 호출되면 터미널에 hello를 출력하는 함수입니다.
    """
    print('hello')

result3 = my_func()
print(result3)




