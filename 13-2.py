f = open("13.txt").read().split("\n\n")


ans = 0

for i in f:
    minPrice = 1000

    i = i.split("\n")
    ax = int(i[0][i[0].index("X")+2:i[0].index(",")])
    ay = int(i[0][i[0].index("Y")+2:])

    bx = int(i[1][i[1].index("X")+2:i[1].index(",")])
    by = int(i[1][i[1].index("Y")+2:])

    tx = int(i[2][i[2].index("X")+2:i[2].index(",")]) + 10000000000000
    ty = int(i[2][i[2].index("Y")+2:]) + 10000000000000

    D = ax*by-ay*bx

    iD = by*tx - bx*ty
    jD = -ay*tx + ax*ty

    if  D == 0:
        continue


    if (iD)%D != 0:
        continue

    if jD % D != 0:
        continue

    ans += (3*iD + jD)//D


        



    
print(ans)



