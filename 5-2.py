f = open("5.txt").read().splitlines()


def cmp(a,b):
    if f"{a}|{b}" in rules:
        return True
    return False


rules, updates = f[:f.index("")], f[f.index("")+1:]

rules = [rule.split("|") for rule in rules]

print


ans = 0
for update in updates:
    update = update.split(",")
    
    valid = True
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[1]) < update.index(rule[0]):
            valid = False
            break
    if not valid:
        sorted = False
        i = 1
        while i < len(update):
            moved = False
            for j in range(len(update)-i):
                if [update[-i], update[j]] in rules:
                    update = update[:j] + [update[-1]] + update[j:-1]
                    moved = True
                    i=1
                    break
            if not moved:
                i += 1
            
        ans += int(update[len(update)//2])
            

print(ans)