# 프로그래머스: 자물쇠와 열쇠
def solution(key, lock):
    answer = False

    total = 0
    len_key = len(key)
    len_lock = len(lock)
    key_list = [[[0 for col in range(len_key)] for row in range(len_key)] for k in range(4)]

    expand_lock = [[-1 for col in range(len_lock + 2 * (len_key - 1))]
                   for row in range(len_lock + 2 * (len_key - 1))]
    for i in range(len_lock):
        total += sum(lock[i])
        expand_lock[i + len_key - 1][len_key - 1:len_key + len_lock - 1] = lock[i]
    total = len_lock ** 2 - total

    for i in range(len_key):
        for j in range(len_key):
            if key[i][j] == 1:
                key_list[0][i][j] = 0
                key_list[1][j][len_key - i - 1] = 0
                key_list[2][len_key - i - 1][len_key - j - 1] = 0
                key_list[3][len_key - j - 1][i] = 0
            else:
                key_list[0][i][j] = 1
                key_list[1][j][len_key - i - 1] = 1
                key_list[2][len_key - i - 1][len_key - j - 1] = 1
                key_list[3][len_key - j - 1][i] = 1

    for i in range(len_lock + len_key - 1):
        for j in range(len_lock + len_key - 1):
            for k in range(4):
                check = True
                for n in range(len_key):
                    for m in range(len_key):
                        if expand_lock[i + n][j + m] != -1 and expand_lock[i + n][j + m] != key_list[k][n][m]:
                            check = False
                            break
                    if check == False:
                        break
                if check:
                    find = 0
                    for x in range(i, i + len_key):
                        for y in range(j, j + len_key):
                            if expand_lock[x][y] == 0:
                                find += 1
                    if find == total:
                        return True
    return answer