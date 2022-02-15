import copy
def front_find_answer(words, q):
    start = 0
    end = len(words) - 1
    while start <= end:
        mid = (start + end) // 2
        if words[mid][:len(q[0])] < q[0]:
            start = mid + 1
        else:
            end = mid - 1

    start2 = 0
    end2 = len(words) - 1
    while start2 <= end2:
        mid2 = (start2 + end2) // 2
        if words[mid2][:len(q[0])] <= q[0]:
            start2 = mid2 + 1
        else:
            end2 = mid2 - 1
    return start2 - start


def solution(words, queries):
    answer = []
    q = []
    for i in queries:
        if i[0] == '?':
            q.append([i.replace('?', '')[::-1],len(i), 1])
        else:
            q.append([i.replace('?', ''), len(i), 0])
    dic = {}
    ric = {}
    for i in words:
        if len(i) in dic:
            dic[len(i)].append(i)
        else:
            dic[len(i)] = [i]
        if len(i) in ric:
            ric[len(i)].append(i[::-1])
        else:
            ric[len(i)] = [i[::-1]]
    for i in dic.values():
        i.sort()
    for i in ric.values():
        i.sort()

    for i in q:
        if i[2] == 0:
            if i[1] in dic:
                answer.append(front_find_answer(dic[i[1]], i))
            else:
                answer.append(0)
        else:
            if i[1] in ric:
                answer.append(front_find_answer(ric[i[1]], i))
            else:
                answer.append(0)
    return answer