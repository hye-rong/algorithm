# 백준 10825번
# 국영수

# sorted()의 key 인자로, 내가 커스텀할 비교 함수를 넣어주면 된다.
# 비교 함수는 비교할 아이템의 요소를 반환하면 된다.
# 비교 함수는 익명 함수(lambda) 도 가능하고, 별도로 정의해도 된다.
# 비교할 아이템의 요소가 복수 개일 경우, 튜플로 그 순서를 내보내주면 된다.
# -를 붙이면, 현재 정렬차순과 반대로 하게 된다.

# 문자열을 정렬하기 위해서는 sorted()를 사용합니다.
# 문자열은 변경을 할 수 없는 이뮤터블형태이기 때문에 sort()를 사용할 수 없습니다.

import sys

n = int(sys.stdin.readline())
student = []
for i in range(n):
    name, l, e, m = sys.stdin.readline().split()
    student.append((int(l), int(e), int(m), name))
student = sorted(student, key = lambda x : (-x[0], x[1], -x[2], x[3]))

for i in student:
    print(i[3])
