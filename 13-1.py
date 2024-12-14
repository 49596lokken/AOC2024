f = open("13.txt").read().split("\n\n")



ans = 0

for i in f:
    minPrice = 1000

    i = i.split("\n")
    ax = int(i[0][i[0].index("X")+2:i[0].index(",")])
    ay = int(i[0][i[0].index("Y")+2:])

    bx = int(i[1][i[1].index("X")+2:i[1].index(",")])
    by = int(i[1][i[1].index("Y")+2:])

    tx = int(i[2][i[2].index("X")+2:i[2].index(",")]) 
    ty = int(i[2][i[2].index("Y")+2:])

    for i in range(101):
        for j in range(101):
            if ax * i + bx*j == tx and ay*i + by*j ==ty and 3*i+j < minPrice:
                minPrice = 3*i+j
    if minPrice != 1000:
        ans += minPrice
print(ans)


