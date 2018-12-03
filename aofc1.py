F = open("input.txt", 'r')
lines = F.readlines()
freq = 0
l = []
l.append(0)
tocontinue = True
while tocontinue:
    #print(str(freq))
    for line in lines:
        freq += int(line)
        if freq in l:
            print(freq)
            tocontinue = False
            break
        l.append(freq)
