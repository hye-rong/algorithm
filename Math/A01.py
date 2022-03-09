# 3343번: 장미
import math

n, a, b, c, d = map(int, input().split())

# 개당 가격이 더 저렴한 걸로 구입
if b/a < d/c:
    one = n//a
    remain -= n//a * a
else:
    two = n//c
    remain -= n//c * c
# 남은 거 어케 살지 고민
if remain != 0:
    if math.ceil(remain/a)*b < math.ceil(remain/c)*d:
        one += math.ceil(remain/a)
    else:
        two += math.ceil(remain/c)
    if one * two != 0: # 두 곳에서 구매
        remain = n - (one*a + two*c)
        if remain > a:
            one -= remain//a
        if remain > c:
            two -= remain//c
print(one*b + two*d)