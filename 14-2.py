f = open("14.txt").read().splitlines()


quads = [0,0,0,0]

robots = []
tree = set()

for i in range(102):
    tree.add((50-i, i))
    tree.add((50+i, i))
tree.add((50, 102))

for line in f:
    pos = tuple(line[line.index("=")+1:line.index(" ")].split(","))
    pos = tuple(int(i) for i in pos)

    line = line[line.index(" "):]
    v = tuple(line[line.index("=")+1:].split(","))
    v = tuple(int(i) for i in v)

    robots.append((pos,v))


i = 0
while True:
    i += 1
    seen = set()
    for j, r in enumerate(robots):
        pos, v = r
        pos = ((pos[0] + v[0])%101, (pos[1]+v[1])%103)
        robots[j] = (pos, v)
        seen.add(pos)
        

    if len(seen) == len(robots):
        print(i)

        for i in range(101):
            for j in range(103):
                if (j, i) in seen:
                    print("#", end="")
                else:
                    print(" ", end="")
            print()
        break

    
    
    


