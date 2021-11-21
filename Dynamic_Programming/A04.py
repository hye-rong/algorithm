# 프로그래머스 동적계획법 N으로 표현

from itertools import product

def solution(N, number):
    if N == number:
        return 1
    dic = {}
    dic[1] = [N]
    num = N
    for i in range(2, 9):
        num = num * 10 + N
        dic[i] = {num}
        for j in range(1, i // 2 + 1):
            pair = product(dic[j], dic[i - j])
            for p in pair:
                a, b = p
                dic[i].add(a + b)
                dic[i].add(a * b)
                if a > b:
                    dic[i].add(a - b)
                    dic[i].add(a // b)
                elif a < b:
                    dic[i].add(b - a)
                    dic[i].add(b // a)
                else:
                    dic[i].add(1)

            if number in dic[i]:
                return i

    return -1