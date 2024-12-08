import numpy as np
f = open("6.txt").read().splitlines()


visited = [[False for j in i] for i in f]


for i in range(len(f)):
    if "^" in f[i]:
        break

dir = np.array([-1,0])

pos = np.array([i, f[i].index("^")])


while pos[0] < len(f) and pos[1] < len(f[i]) and pos[0] >= 0 and pos[1] >= 0:
    visited[pos[0]][pos[1]] = True
    nextPos = pos + dir
    if nextPos[0] >= len(f) or nextPos[0] < 0 or nextPos[1] >= len(f) or nextPos[1] < 0:
        break
    while f[nextPos[0]][nextPos[1]] == "#":
        dir = (np.array([[0, 1], [-1, 0]]) @ dir.T).T
        nextPos = pos + dir
    pos = pos + dir


print(sum(sum(i) for i in visited))