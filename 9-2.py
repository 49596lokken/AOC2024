f = open("9.txt").read()

#f = """2333133121414131402"""

n = 0
blocks = []
fileSizes = []
gapSizes = []

for i in range(len(f)//2+1):
    fileSizes.append(int(f[2*i]))
    for _ in range(fileSizes[-1]):
        blocks.append(i)
    if 2*i+1 < len(f):
        gap = int(f[2*i+1])
        gapSizes.append(gap)
        blocks.append(".")

blocks.append(".")
gapSizes.append(0)

while fileSizes:

    for i in range(len(fileSizes)-1):
        
        if gapSizes[i] >= fileSizes[-1]:
            gap = 0
            for j in range(len(blocks)):
                if blocks[j] == ".":
                    if gap == len(fileSizes)-1:
                        break
                    gap += 1
            
            if blocks[j-1] == len(fileSizes)-1:
                gapSizes[len(fileSizes)-2] += gapSizes[len(fileSizes)-1] + fileSizes[-1]
                gapSizes = gapSizes[:len(fileSizes)-1] + gapSizes[len(fileSizes):]
            else:
                gapSizes[len(fileSizes)-2] += fileSizes[-1]

            while len(fileSizes)-1 in blocks:
                blocks.remove(len(fileSizes)-1)
            

            for j in range(len(blocks)-1):
                if blocks[j] == "." and blocks[j+1] == ".":
                    blocks = blocks[:j] + blocks[j+1:]
                    break

            gapSizes[i] -= fileSizes[-1]
            gapNum = 0

            for j in range(len(blocks)):
                if blocks[j] == ".":
                    if gapNum == i:
                        break
                    gapNum += 1
        

            for _ in range(fileSizes[-1]):
                blocks = blocks[:j] + [len(fileSizes)-1] + blocks[j:]

            break
    fileSizes = fileSizes[:-1]
    if len(fileSizes)%100 == 0:
        print(f"{100-len(fileSizes)//100}%")


ans = 0

gap = 0
gapAdj = 0
for i in range(len(blocks)):
    if blocks[i] == ".":
        gapAdj += gapSizes[gap]-1
        gap += 1
        continue

    #print((i + gapAdj), blocks[i])
    ans += (i + gapAdj) * blocks[i] 

print(ans)



    
