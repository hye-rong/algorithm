# 백준 1038번: 감소하는 수

# 0-9까지의 숫자중 k를 고르는 방법의 수
# k자리에서 몇 개 나오는지랑 같음
import itertools
n = int(input())
numbers = [i for i in range(10)]
cnt = 0
for i in range(1, 11):
    nCr = itertools.combinations(numbers, i)
    nCr = list(nCr)
    l = len(nCr)
    if cnt + l > n:
        # i자리 숫자 중에서 n - cnt 번째
        tmp = []
        for nums in nCr:
            arr = list(nums)
            arr.sort(reverse=True)
            ans = 0
            for k in arr:
                ans = ans*10 + k
            tmp.append(ans)
        tmp.sort()
        print(tmp[n-cnt])
        break
    else:
        cnt += l
else:
    print(-1)
