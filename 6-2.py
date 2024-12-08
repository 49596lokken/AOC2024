import numpy as np
import copy
f = open("6.txt").read().splitlines()


def checkLoop(f):
    visited = [[0 for j in i] for i in f]
    for i in range(len(f)):
        if "^" in f[i]:
            break

    dir = np.array([-1,0])
    pos = np.array([i, f[i].index("^")])

    while inside(pos, f):
        visited[pos[0]][pos[1]] += 1
        if visited[pos[0]][pos[1]] > 4:
            return True
        nextPos = pos + dir
        

        if not inside(nextPos, f):
            return False

        while f[nextPos[0]][nextPos[1]] == "#":
            dir = (np.array([[0, 1], [-1, 0]]) @ dir.T).T
            nextPos = pos + dir
            

        pos += dir



def inside(pos, f):
    return pos[0] < len(f) and pos[1] < len(f[0]) and pos[0] >= 0 and pos[1] >= 0

visited = [[[] for j in i] for i in f]
path = []


for i in range(len(f)):
    if "^" in f[i]:
        break

dir = np.array([-1,0])
pos = np.array([i, f[i].index("^")])

initPos = tuple(pos)




ans = 0

path = set()
while inside(pos, f):

    nextPos = pos + dir

    if not inside(nextPos, f):
        break

    while f[nextPos[0]][nextPos[1]] == "#":
        dir = (np.array([[0, 1], [-1, 0]]) @ dir.T).T
        nextPos = pos + dir


    pos += dir
    path.add(tuple(pos))

            
path = list(path)
i = 0
while i < len(path):
    node = path[i]
    if node == initPos:
        path = path[:i] + path[i+1:]
        i -= 1 
    i += 1


n = 0
lastpc = 0
for node in path:
    f_new = f[:]

    f_new[node[0]] = f_new[node[0]][:node[1]] + "#" + f_new[node[0]][node[1]+1:]

    if checkLoop(f_new):
        ans += 1

    n += 1
    if (100*n)//len(path) > lastpc:
        print(f"{(100*n)//len(path)}%")
        lastpc = (100*n)//len(path)
    
    
print(ans)



