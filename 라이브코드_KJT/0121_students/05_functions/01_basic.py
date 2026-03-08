# 함수 정의

# 함수 호출 및 반환 값 할당

# [번외] print() 함수는 반환값이 없다.
def get_sum(a,b):
    """
    이것은 두 수를 파라미터로 받아
    두 수의 합을 반환하는 함수입니다.
    ...make_sum(1,2)
    3
    
    :param a: Description
    :param b: Description
    """
    result = a + b
    return result

result_1 = get_sum(6,7)
result_2 = get_sum(20,7)

print(result_1)  
print(get_sum(10,5))  # 15
print(result_2) 
print(get_sum(result_1, result_2))  # 33



def greet(name, age=30):
        print(f'안녕하세요, {name}님  {age}살이시군요')

greet('철수')  # 기본값 사용
greet('영희', 25)  # age 매개변수에 값 전달
print(greet)