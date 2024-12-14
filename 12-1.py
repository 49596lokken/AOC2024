f = open("12.txt").read().splitlines()



regions = []
used = [[False for _ in i] for i in f]


def get_neighbours(i,j):
    n = []
    if i>=1:
        n.append((i-1, j))
    if i+1<len(f):
        n.append((i+1, j))
    if j >=1:
        n.append((i,j-1))
    if j+1<len(f):
        n.append((i,j+1))
    return n

def get_region(i,j):
    r = []
    for i1,j1 in get_neighbours(i,j):
        if used[i1][j1]:
            continue
        if f[i1][j1] == f[i][j]:
            r.append((i1,j1))
            used[i1][j1] = True
            r.extend(get_region(i1,j1))
    return r


for i in range(len(f)):
    for j in range(len(f[i])):
        if used[i][j]:
            continue
        r = [(i,j)]
        used[i][j] = True
        r.extend(get_region(i,j))
        regions.append(r)


def calculate_perimeter(region):
    bad_neighbours = []

    for point in region:
        for k in [-1j**i for i in range(4)]:
            if (int(k.real) + point[0], int(k.imag + point[1])) in region:
                continue
            bad_neighbours.append((int(k.real) + point[0], int(k.imag + point[1])))
    return len(bad_neighbours)

ans = 0
for region in regions:
    ans += len(region)* calculate_perimeter(region)



print(ans)