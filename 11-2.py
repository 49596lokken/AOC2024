f = open("11.txt").read()



stones = f.split(" ")
stones = {int(i):1 for i in stones}
stones 

def blink(stones):
    new = {}

    for stone in stones:
        if stone == 0:
            if 1 in new:
                new[1] += stones[stone]
            else:
                new[1] = stones[stone]
        elif len(str(stone)) %2 == 0:

            a = len(str(stone))//2
            n1, n2 = int(str(stone)[:a]), int(str(stone)[a:])
            if n1 in new:
                new[n1] += stones[stone]
            else:
                new[n1] = stones[stone]
            if n2 in new:
                new[n2] += stones[stone]
            else:
                new[n2] = stones[stone]
            
        else:
            if 2024*stone in new:
                new[2024*stone] += stones[stone]
            else:
                new[2024*stone] = stones[stone]
    
    return new


for i in range(75):
    stones = blink(stones)

print(sum(stones[i] for i in stones))