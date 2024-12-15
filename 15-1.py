f = open("15.txt").read()




f = f.split("\n\n")

grid = f[0].splitlines()

moves = f[1].replace("\n", "")

boxes = []
walls = []

for i in  range(len(grid)):
    if "@" in grid[i]:
        robot = (i, grid[i].index("@"))


for i in range (len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "#":
            walls.append((i,j))
        if grid[i][j] == "O":
            boxes.append((i,j))


dirs = {"<":(0, -1), "^":(-1, 0), ">":(0, 1), "v":(1, 0)}

for move in moves:
    dir = dirs[move]
    nextPos = robot[0] + dir[0],  robot[1] + dir[1]
    if nextPos in walls:
        continue
    if nextPos in boxes:
        nextPos = nextPos[0] + dir[0],  nextPos[1] + dir[1]
        while nextPos in boxes:
            nextPos = nextPos[0] + dir[0], nextPos[1] + dir[1]
        if nextPos in walls:
            continue
        boxes.append(nextPos)
        boxes.remove((robot[0] + dir[0], robot[1] + dir[1]))
        robot = robot[0] + dir[0],  robot[1] + dir[1]
        continue
            
    robot = nextPos

ans = 0
for i,j in boxes:
    ans += 100*i + j

print(ans)
