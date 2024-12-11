f = open("9.txt").read()

#f = """2333133121414131402"""

n = 0
blocks = []
numberCounts = []
numberDots = []

for i in range(len(f)//2+1):
    numberCounts.append(int(f[2*i]))
    if 2*i+1 < len(f):
        numberDots.append(int(f[2*i+1]))

for i in range(len(numberCounts)):
    for _ in range(numberCounts[i]):
        blocks.append(i)
        numberCounts[i]-= 1
    
    if i == len(numberCounts)-1:
        break
    while numberDots[i] > 0 and False in [i==0 for i in numberCounts]:
        for k in range(len(numberCounts)-1, -1, -1):
            if numberCounts[k] != 0:
                numberDots[i] -= 1  
                blocks.append(k)
                numberCounts[k] -= 1
                break

ans = 0
for i in range(len(blocks)):
    ans += i*blocks[i]

print(ans)
    
