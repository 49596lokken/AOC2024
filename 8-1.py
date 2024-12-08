f = open("8.txt").read()



waves = set(f) - set(".")

f = f.splitlines()

nodes = {w:[] for w in waves}

for i in range(len(f)):
    for j in range(len(f[i])):
        if f[i][j] in waves:
            nodes[f[i][j]].append(complex(i, j))


def isIn(pos, g):
    return pos.real < len(g) and pos.imag < len(g[0]) and pos.real >=0 and pos.imag >=0

antinodes = set()


for w in waves:

    for node in nodes[w]:
        temp = nodes[w][:]
        print(temp)
        temp.remove(node)
        for node2 in temp:
            an1 = 2*node - node2
            an2 = 2*node2 - node

            if isIn(an1, f):
                antinodes.add(an1)
            if isIn(an2, f):
                antinodes.add(an2)

print( len(antinodes))
        