from collections import Counter

F = open("inputday2.txt", 'r')
lines = F.readlines()
print(lines)
similar = []
i = 0
lines.sort()
while i < len(lines) - 2:
    c = 0
    differences = 0
    same = ''
    first = ''
    second = ''
    if lines[i].endswith('\n'):
        first = lines[i][:-1]
    if lines[i + 1].endswith('\n'):
        second = lines[i + 1][:-1]
    while c < min(len(first), len(second)):
        if first[c] != second[c]:
            differences += 1
        c += 1
    if differences == 1:
        print(lines[i] + " minus " + str(c))
        print(lines[i + 1] + " minus " + str(c))
    i += 1