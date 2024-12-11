f = open("10.txt").read().splitlines()




f = [[int(j) if j.isnumeric() else -4 for j in i] for i in f]



score = [[0 for j in i] for i in f]
nines = []
for i in range(len(f)):
    for j in range(len(f)):
        
        if f[i][j] == 9:
            nines.append(complex(i,j))


scores = {}

def neighbours(x: complex) -> list[complex]:
    n = []
    for i in range(int(x.real)-1, int(x.real)+2):
        if i < 0 or i >= len(f):
            continue
        n.append(complex(i, x.imag))

    for j in range(int(x.imag)-1, int(x.imag)+2):
        if j < 0 or j >= len(f[int(x.real)]):
            continue
        n.append(complex(x.real,j))
    return n
5
ans = 0
for nine in nines:
    to_explore = {nine}
    seen = []
    seen.append(nine)
    scores = {}
    print(f"Starting {nine}")
    while to_explore:
        x = next(iter(to_explore))
        to_explore = to_explore - {x}
        for n in neighbours(x):
            if f[int(n.real)][int(n.imag)] - f[int(x.real)][int(x.imag)] == -1 and not n in seen:
                to_explore.add(n)
                seen.append(n)
                if f[int(n.real)][int(n.imag)] == 0:
                    ans += 1
                    if n in scores:
                        scores[n] += 1
                        print("UwU")
                    else:
                        scores[n] = 1
                    print(n)
                    


print(ans)
print(scores)
