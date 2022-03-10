# 백준 2504번: 괄호의 값

import sys
stack = []

str = sys.stdin.readline().rstrip()
stack.append(str[0])

for i in range(1, len(str)):
    ch = str[i] # stack에 넣을 값
    cur = 1
    if ch == '(' or ch == '[':
        stack.append(ch)
    elif ch == ')' or ch == ']': # ) or ]
        if stack: # 비어있지 않은 경우
            a = stack.pop()
            if type(a) == int:
                cur = a
                if stack:
                    a = stack.pop()
                else:
                    print(0)
                    sys.exit()
            if a == '(' and ch == ')':
                cur = cur * 2
            elif a == '[' and ch == ']':
                cur = cur * 3
            else:
                break
            if stack and type(stack[-1]) == int:
                cur += stack.pop()
            stack.append(cur)
        else: # 실패
            print(0)
            sys.exit()
    else:
        print(0)
        sys.exit()


if len(stack) == 1 and type(stack[0]) == int:
    print(stack.pop())
else:
    print(0)

