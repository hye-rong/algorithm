# 백준 1062번: 가르침

# a c n t i 5개를 가르치면 0(k>=5)
# 글자 받으면서 앞 뒤는 자른다
# 나머지 글자도 set으로 받아서 중복 제거
# 또 set(a,c,n,t,i)를 해서 필요한 글지만 남긴다

# combination에서 n보다 k가 더 큰 경우를 고려해야한다

import itertools

n, k = map(int, input().split())
if k < 5:
    print(0)
    exit(0)
if k == 26:
    print(n)
    exit(0)
k -= 5
basic = {'a', 'n', 't', 'c', 'i'}
words = []
all = set()
for i in range(n):
    str = input()
    s = set(str[4:-4])-basic # 중복과 기본 글자 제거
    if len(s) <= k: # k개의 글자로 안되는 단어는 미리 제거
        words.append(s)
        all.update(s)
answer = 0
if k >= len(all):
    print(len(words))
    exit(0)
nCr = itertools.combinations(all, k)
for i in nCr:
    tmp = 0
    for word in words:
        check = len(word)
        for w in word:
            if w in i:
                check -= 1
            else:
                break
        if check == 0:
            tmp += 1
    answer = max(tmp, answer)
print(answer)

