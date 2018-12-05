F = open("inputday5.txt", 'r')

data = F.readlines()
polymer = data[0]

tocontinue = True
changes = 0
print(str(len(polymer)))
while tocontinue:
    changes = 0
    i = 0
    while i < len(polymer) - 1:
        if polymer[i].islower() and polymer[i + 1].isupper() and polymer[i].lower() == polymer[i + 1].lower():
            changes += 1
            #print("Making changes")
            polymer = polymer[:i] + polymer[i + 2:]
            i += 1
        elif polymer[i].isupper() and polymer[i + 1].islower() and polymer[i].lower() == polymer[i + 1].lower():
            changes += 1
            polymer = polymer[:i] + polymer[i + 2:]
            i += 1
        else:
            i += 1

    if changes == 0:
        tocontinue = False
        print(polymer)
        print(str(len(polymer)))
        #33830 is too high!

