f = open("2.txt").readlines()


def checkSafe(line):
    safe = True
    for j in range(1, len(line)):
        if (line[j] - line[j-1]) * (line[1]-line[0]) <= 0:
            safe = False
            break
        if abs(line[j] - line[j-1]) > 3:
            safe = False
            break
    return safe



ans = 0
for i in f:
    i = [int(j) for j in i.split(" ")]
    safe = checkSafe(i)

    ans += safe
    if not safe:
        for j in range(len(i)):
            i_new = i[:j] + i[j+1:]
            if checkSafe(i_new):
                ans += 1
                break

print(ans)