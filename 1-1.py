f = open("1.txt").readlines()




f = [i.split("   ") for i in f]


f = [[int(f[i][j]) for i in range(len(f))] for j in range(2)]


ans = 0

while len(f[0]):
    ans += abs(min(f[0]) - min(f[1]))
    f[0].remove(min(f[0]))
    f[1].remove(min(f[1]))

print(ans)

