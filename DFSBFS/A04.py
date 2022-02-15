def solution(p):
    return checkStr(p)

def checkStr(str):
    check = 0
    if str == '':
        return str
    idx = 0
    for i in range(len(str)):
        if str[i] == '(':
            check += 1
        else:
            check -= 1
        if check == 0:
            idx = i
            break
    if str[0] == '(':
        return str[0:i+1] + checkStr(str[i+1:])
    else:
        reverse = []
        for i in range(1, idx):
            if str[i] == '(':
                reverse.append(')')
            else:
                reverse.append('(')
        return '(' + checkStr(str[idx+1:])+')'+''.join(reverse)