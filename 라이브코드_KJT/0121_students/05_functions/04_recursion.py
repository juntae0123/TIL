def factorial(n):
    # 종료 조건: n이 0이면 1을 반환
    if n == 0:
        return 1
    else:
        # 재귀 호출: n과 n-1의 팩토리얼을 곱한 결과를 반환
        return n * factorial(n - 1)


# 팩토리얼 계산 예시
print(factorial(5))  # 120

def factorial(k):
    if k == 1:
        return 1
    else:
        return k * factorial(k - 1)
print(factorial(6))  # 720

def pibonacci(s):
    if s == 1:
        return 1
    elif s == 2:
        return 1
    else:
        return pibonacci(s-1) + pibonacci(s-2)
print(pibonacci(7))  # 13