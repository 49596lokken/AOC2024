f = open("1.txt").readlines()




f = [i.split("   ") for i in f]


f = [[int(f[i][j]) for i in range(len(f))] for j in range(2)]


ans = 0

for i in f[0]:
    ans += i*f[1].count(i)
print(ans)

