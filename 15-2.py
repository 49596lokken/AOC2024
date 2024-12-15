f = open("15.txt").read()

f = f.split("\n\n")

grid = f[0]
grid = f[0].replace(".", "..").replace("O", "[]").replace("#", "##").replace("@", "@.")
grid = grid.splitlines()

moves = f[1].replace("\n", "")

lboxes = []
rboxes = []
walls = []

for i in  range(len(grid)):
    if "@" in grid[i]:
        robot = (i, grid[i].index("@"))


for i in range (len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            walls.append((i,j))
        if grid[i][j] == "[":
            lboxes.append((i,j))
            rboxes.append((i, j+1))


dirs = {"<":(0, -1), "^":(-1, 0), ">":(0, 1), "v":(1, 0)}


def canPush(box, dir):
    if (box[0] + dir[0], box[1]) in walls or (box[0] + dir[0], box[1]+1) in walls:
        return False
    can = True
    if (box[0] + dir[0], box[1]) in lboxes:
        can &= canPush((box[0] + dir[0], box[1]), dir)
    if (box[0] + dir[0], box[1]) in rboxes:
        can &= canPush((box[0] + dir[0], box[1]-1), dir)
    if (box[0] + dir[0], box[1] + 1) in lboxes:
        can &= canPush((box[0] + dir[0], box[1]+1), dir)
    return can

def push(box, dir):
    if (box[0] + dir[0], box[1]) in lboxes:
        push((box[0] + dir[0], box[1]), dir)
    if (box[0] + dir[0], box[1]) in rboxes:
        push((box[0] + dir[0], box[1]-1), dir)
    if (box[0] + dir[0], box[1] + 1) in lboxes:
        push((box[0] + dir[0], box[1]+1), dir)
    
    lboxes.remove(box)
    rboxes.remove((box[0], box[1]+1))
    lboxes.append((box[0]+dir[0], box[1]))
    rboxes.append((box[0]+dir[0], box[1]+1))

for move in moves:
    
    out = ""
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i,j) == robot:
                out += "@"
            elif (i,j) in walls:
                out += "#"
            elif (i,j) in lboxes:
                out += "["
            elif (i,j) in rboxes:
                out += "]"
            else:
                out += "."
        out += "\n"
    print(out)
    #print("Now move", move)
    dir = dirs[move]
    nextPos = robot[0] + dir[0],  robot[1] + dir[1]
    if nextPos in walls:
        continue
    if nextPos in lboxes:
        if move == ">":
            nextPos = nextPos[0] + 2*dir[0],  nextPos[1] + 2*dir[1]
            while nextPos in lboxes:
                nextPos = nextPos[0] + 2*dir[0], nextPos[1] + 2*dir[1]
            if nextPos in walls:
                continue
            for i in range(nextPos[1] - robot[1], 0 , -1):
                if i % 2 == 0:
                    lboxes.append((robot[0], robot[1]+i))
                    rboxes.remove((robot[0], robot[1]+i))
                else:
                    rboxes.append((robot[0], robot[1]+i))
                    if (robot[0], robot[1]+i) in lboxes:
                        lboxes.remove((robot[0], robot[1]+i))
            robot = robot[0] + dir[0],  robot[1] + dir[1]
            rboxes.remove(robot)
            continue

        # Move up or down
        if canPush(nextPos, dir):
            push(nextPos, dir)
            robot = nextPos
            
        continue

    if nextPos in rboxes:
        if move == "<":
            nextPos = nextPos[0] + 2*dir[0],  nextPos[1] + 2*dir[1]
            while nextPos in rboxes:
                nextPos = nextPos[0] + 2*dir[0], nextPos[1] + 2*dir[1]
            if nextPos in walls:
                continue


            for i in range(robot[1] - nextPos[1],0, -1):
                if i % 2 == 0:
                    rboxes.append((robot[0], robot[1]-i))
                    lboxes.remove((robot[0], robot[1]-i))
                else:
                    lboxes.append((robot[0], robot[1]-i))

                    if (robot[0], robot[1]-i) in rboxes:
                        rboxes.remove((robot[0], robot[1]-i))

            robot = robot[0] + dir[0],  robot[1] + dir[1]
            lboxes.remove(robot)
            continue

        # Move up or down
        if canPush((nextPos[0], nextPos[1]-1), dir):
            push((nextPos[0], nextPos[1]-1), dir)
            robot = nextPos
        continue

            

        
            
    robot = nextPos

ans = 0
for i,j in lboxes:
    ans += 100*i + j

print(ans)
