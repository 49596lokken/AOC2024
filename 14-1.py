f = open("14.txt").read().splitlines()






quads = [0,0,0,0]

for line in f:
    pos = tuple(line[line.index("=")+1:line.index(" ")].split(","))
    pos = tuple(int(i) for i in pos)

    line = line[line.index(" "):]
    v = tuple(line[line.index("=")+1:].split(","))
    v = tuple(int(i) for i in v)

    for i in range(100):
        pos = ((pos[0] + v[0])%101, (pos[1]+v[1])%103)
        
    
    if pos[0] < 50:
        if pos[1] < 51:
            quads[0] += 1
        elif pos[1] > 51:
            quads[1] += 1
    elif pos[0] > 50:
        if pos[1] < 51:
            quads[2] += 1
        elif pos[1] > 51:
            quads[3] += 1


print(quads[0]*quads[1]*quads[2]*quads[3])