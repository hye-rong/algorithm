from itertools import combinations
import copy

def play(tmap, tloc):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for tx, ty in tloc:
        for i in range(4):
            cx, cy = tx, ty
            while True:
                cx += dx[i]
                cy += dy[i]
                if tmap[cx][cy] == 'X':
                    pass
                elif tmap[cx][cy] == -1:
                    break
                elif tmap[cx][cy] == 'T':
                    break
                else:
                    return False
    return True

if __name__ == '__main__':
    n = int(input())
    cmap = [[-1 for i in range(n+2)] for j in range(n+2)]
    tloc = []
    xloc = []

    for i in range(n):
        cmap[i+1][1:-1] = input().split()
        for j in range(n):
            if cmap[i+1][j+1] == 'T':
                tloc.append([i+1, j+1])
            elif cmap[i+1][j+1] == 'X':
                xloc.append([i+1, j+1])
    comb = combinations(xloc, 3)

    check = False
    for loc in comb:
        tmap = copy.deepcopy(cmap)
        for x, y in loc:
            tmap[x][y] = -1
        check = play(tmap, tloc)
        if check:
            print("YES")
            break
    if not check:
        print("NO")