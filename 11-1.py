f = open("11.txt").read()



stones = f.split(" ")
stones = [int(i) for i in stones]


def blink(stones):
    new = []
    for stone in stones:
        if stone == 0:
            new.append(1)
        elif len(str(stone)) %2 == 0:

            a = len(str(stone))//2
            new.append(int(str(stone)[:a]))
            new.append(int(str(stone)[a:]))
        else:
            new.append(2024 * stone)
    
    return new


for i in range(25):
    stones = blink(stones)
    new = {}
    for stone in stones:
        if stone in new:
            new[stone] += 1
        else:
            new[stone] = 1
    print(new)
    if i == 2:
        break