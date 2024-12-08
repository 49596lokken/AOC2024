f = open("7.txt").read().splitlines()


def check(test, numbers):
    if len(numbers) == 1:
        return test == numbers[-1]
    
    ans = 0
    if test%numbers[-1] == 0:
        ans = check(test//numbers[-1], numbers[:-1])
    
    return ans + check(test-numbers[-1], numbers[:-1])

ans = 0
for line in f:
    test, numbers = line.split(": ")
    test = int(test)

    numbers = [int(i) for i in numbers.split(" ")]

    if check(test, numbers):
        ans += test

print(ans)