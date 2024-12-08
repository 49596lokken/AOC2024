f = open("3.txt").read()




ans = 0

doing = 1

for i in range(len(f)):
    if f[i:].startswith("do()"):
        doing = 1
    elif f[i:].startswith("don't()"):
        doing = 0

    if f[i:i+4] == "mul(":
        if "," in f[i+5:]:
            com =  f.index(",", i)
            if f[i+4:com].isnumeric():
                if ")" in f[com:]:
                    if f[com+1:f.index(")", com)].isnumeric():
                        ans += int(f[i+4:com]) * int(f[com+1:f.index(")", com)]) * doing



print(ans)


