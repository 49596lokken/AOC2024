f = open("5.txt").read().splitlines()




rules, updates = f[:f.index("")], f[f.index("")+1:]

rules = [rule.split("|") for rule in rules]


ans = 0
for update in updates:
    update = update.split(",")
    valid = True
    for rule in rules:
        if rule[0] in update and rule[1] in update and update.index(rule[1]) < update.index(rule[0]):
            valid = False
            break
    if valid:
        ans += int(update[len(update)//2])

print(ans)