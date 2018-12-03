import re

F = open("inputday3.txt", 'r')
boxes = []
for i in range(1000):
    curlist = []
    for x in range(1000):
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

    print(str(x) + " is x " + str(y) + " is y" + " bottom " + str(bottom) + " right " + str(right))
    while y <= bottom:
        while x <= right:
            if str(boxes[x][y]).strip().isdigit():
                counter += 1
            else:
                boxes[x][y] = number
                print("in here!")
            x += 1
        y += 1
    #print("Number " + number + " Left edge " + leftedge + " top edge " + topedge + " width " + width + " height " + height)

#print(lines)
print(counter)
print(boxes[35])