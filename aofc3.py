import re

F = open("inputday3a.txt", 'r')
boxes = []
for i in range(8):
    curlist = []
    for x in range(8):
         curlist.append(".")
    boxes.append(curlist)

lines = F.readlines()
counter = 0
for line in lines:
    a = re.split('@|,:', line)
    number = a[0][1:]
    next = re.split(':', a[1])
    edges = next[0].split(',')
    leftedge = int(edges[0])
    topedge = int(edges[1])

    dimens = next[1].split("x")
    width = int(dimens[0])
    height = int(dimens[1])
    bottom = topedge + height
    right = leftedge + width
    x = leftedge
    y = topedge

    while y < bottom:
        while x < right:
            if str(boxes[y][x]).strip().isdigit():
                counter += 1
                boxes[y][x] = 'X'
            else:
                boxes[y][x] = number
            x += 1
        y += 1
        x = leftedge

    #print("Number " + number + " Left edge " + leftedge + " top edge " + topedge + " width " + width + " height " + height)

#print(lines)

for i, count in enumerate(range(len(boxes))):
    print(str(count) + " : ", end = '')
    for j in range(len(boxes[i])):
        print(boxes[i][j], end = '')
    print("\n")

print(counter)