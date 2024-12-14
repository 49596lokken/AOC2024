f = open("12-test.txt").read().splitlines()


regions = []
used = [[False for _ in i] for i in f]


def get_neighbours(i,j):
    n = []
    if i>=1:
        n.append([i-1, j])
    if i+1<len(f):
        n.append([i+1, j])
    if j >=1:
        n.append([i,j-1])
    if j+1<len(f):
        n.append([i,j+1])
    return n

def get_region(i,j):
    r = []
    for i1,j1 in get_neighbours(i,j):
        if used[i1][j1]:
            continue
        if f[i1][j1] == f[i][j]:
            r.append([i1,j1])
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




def count_corners(i):
    if corners[i] != 0:
        return corners[i]
    numCorn = 0
    for j in enclaves[i]:
        numCorn += count_corners(j)
        corners[j] = count_corners(j)
        
    point = region[0][:]
    start = point[:]
    dirs = [[0,1], [1,0], [0,-1], [-1, 0]]
    letter = f[point[0]][point[1]]
    dir = 0
    while True:
        point[0] += dirs[dir][0]
        point[1] += dirs[dir][1]
        
        if point[0] >= len(f) or point[0] < 0 or point[1] >= len(f[point[0]]) or point[1] < 0:
            numCorn += 1
            point[0] -= dirs[dir][0]
            point[1] -= dirs[dir][1]
            dir += 1
            dir %= 4

        if f[point[0]][point[1]] != letter:
            numCorn += 1
            point[0] -= dirs[dir][0]
            point[1] -= dirs[dir][1]
            dir += 1
            dir %= 4
        
        #Check for reflex angle
        dir += 3
        dir %= 4
    
        point[0] += dirs[dir][0]
        point[1] += dirs[dir][1]
        
        if point[0] >= len(f) or point[0] < 0 or point[1] >= len(f[point[0]]) or point[1] < 0 or f[point[0]][point[1]] != letter:
            # No reflex angle
            point[0] -= dirs[dir][0]
            point[1] -= dirs[dir][1]
            dir += 1
            dir %= 4
        else:
            numCorn += 1
        
        if point == start and dir == 0:
            corners[i] = numCorn
            return
            
    

ans = 0
# Work out when a region is inside another
enclaves = [[] for _ in regions]


for i, region in enumerate(regions):
    neighbouring = set()
    for r in region:
        neighbours = get_neighbours(r[0], r[1])
        if len(neighbours) != 4:
            neighbouring.add(-1)
        for n in neighbours:
            if n in region:
                continue
            
            for j, n_region in enumerate(regions):
                if n in n_region:
                    neighbouring.add(j)
    if len(neighbouring) == 1:
        enclaves[next(iter(neighbouring))].append(i)
        

corners = [0 for _ in regions]

for i in range(len(regions)):
    region = regions[i]
    count_corners(i)
    ans += len(region) * corners[i]
    
    print(f[region[0][0]][region[0][1]], len(region), corners[i])



print(ans)