# 백준 3745번: 오름세
import sys
while True:
    str = sys.stdin.readline()
    if str == '':
        break
    n = int(str)
    day = list(map(int, sys.stdin.readline().split()))
    check = [day[0]]
    for i in range(1, len(day)):
        if check[-1] < day[i]:
            check.append(day[i])
        elif check[-1] == day[i]:
            check[-1] = day[i]
        else:
            # 이분 탐색해서 들어갈 위치 정함
            start = 0
            end = len(check) - 1
            while start <= end:
                mid = (start + end) // 2
                if check[mid] == day[i]:
                    end = mid - 1
                    break
                elif check[mid] < day[i]:
                    start = mid + 1
                else:
                    end = mid - 1
            check[end+1] = day[i]
    print(len(check))

