f = open("4.txt", "r").readlines()
print(f)

ans = 0

for i in range(1,len(f)-1):
    for j in range(1, len(f[i])-1):
        if f[i][j] == "A":

            if set((f[i-1][j-1], f[i+1][j+1])) == set("MS") and set((f[i-1][j+1], f[i+1][j-1])) == set("MS"):
                ans += 1


print(ans)
