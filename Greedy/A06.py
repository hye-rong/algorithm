# 섬 연결하기
# kruskal Alg
def solution(n, costs):
    answer = 0
    costs = sorted(costs, key=lambda x: x[2])
    node_list = []

    while True:
        a, b, cost = costs.pop(0)
        i = j = -1
        for num in range(len(node_list)):
            if a in node_list[num]:
                i = num
            if b in node_list[num]:
                j = num

        if i == j and i != -1:
            pass
        else:
            if i == -1 and j == -1:
                node_list.append([a, b])
            elif i == -1:
                node_list[j].append(a)
            elif j == -1:
                node_list[i].append(b)
            else:
                tmp = node_list[j]
                node_list[i].extend(tmp)
                node_list.remove(tmp)
            answer += cost

        if len(node_list[0]) == n:
            break

    return answer