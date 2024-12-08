f = open("2.txt").readlines()



ans = 0
for i in f:
    i = [int(j) for j in i.split(" ")]
    safe = True
    for j in range(1, len(i)):
        if (i[j] - i[j-1]) * (i[1]-i[0]) <= 0:
            safe = False
            break
        if abs(i[j] - i[j-1]) > 3:
            safe = False
            break
    
    ans += safe

print(ans)