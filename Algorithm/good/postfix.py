infix = []
postfix = []

stack = []

#괄호 때문에 우선순위가 달라져야 해서 우선순위를 두 개로 나눔.
icp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3}
    #'(' 이 새로 들어올 때 무조건 push
isp = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    #'(' 는 연산이 아니라 "괄호 경계"라서 스택 안에서는 pop되지 않게(우선순위 최저로) 둔다

for ch in infix: # infix 탐색
    if ch.isdigit(): # ch가 숫자일때 (보통 숫자가 먼저나옴 아니면 에러임)
        postfix.append(ch) # postfix에 숫자 push
        #이제 연산을 받고 postfix에 다음 숫자 추가
        #분기점 만약 다음 연산이 우선순위가 더 낮다면 그 다음 연산 또 보는거 반복
        # (우선순위 비교는 숫자랑 하는 게 아니라, "연산자를 만났을 때" 스택 top 연산자와 현재 연산자를 비교한다)
        #isp[stack[-1]] >= icp[ch]
        # 괄호는 postfix에 추가하지않음 -> stack에서만 존재후 순서되면 pop만써서 제거

    elif ch == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop()) # 괄호 안에있던 연산을 이제 꺼낸다~
        stack.pop() # '(' 제거

    else:   # '('나 연산 문자
        while stack and isp[stack[-1]] >= icp[ch]:
        # 연산의 우선순위 비교 : 스택의 마지막 연산자(top)가 현재 ch보다 우선순위가 크거나 같으면 먼저 pop해서 postfix에 넣는다
            postfix.append(stack.pop())
        stack.append(ch) # pop이 끝나면 현재 ch를 스택에 추가

while stack:
    postfix.append(stack.pop())   #  스택 비우기