from string import ascii_lowercase
from string import ascii_uppercase

F = open("inputday5.txt", 'r')

data = F.readlines()
polymer = data[0]

alpha_list_lower = []
alpha_list_upper = []

for c in ascii_lowercase:
    alpha_list_lower.append(c)

for c in ascii_uppercase:
    alpha_list_upper.append(c)

print(alpha_list_upper)
sizes = []
for i in range(len(alpha_list_upper)):
    tocheck = polymer
    tocheck = tocheck.replace(alpha_list_lower[i], "")
    tocheck = tocheck.replace(alpha_list_upper[i], "")
    tocontinue = True
    while tocontinue:
        changes = 0
        i = 0
        while i < len(tocheck) - 1:
            if tocheck[i].islower() and tocheck[i + 1].isupper() and tocheck[i].lower() == tocheck[i + 1].lower():
                changes += 1
                # print("Making changes")
                tocheck = tocheck[:i] + tocheck[i + 2:]
                i += 1
            elif tocheck[i].isupper() and tocheck[i + 1].islower() and tocheck[i].lower() == tocheck[i + 1].lower():
                changes += 1
                tocheck = tocheck[:i] + tocheck[i + 2:]
                i += 1
            else:
                i += 1

        if changes == 0:
            tocontinue = False
            print(tocheck)
            print(str(len(tocheck)))
            # 33830 is too high!

    print(tocheck)
    sizes.append(len(tocheck))
print(sizes)
print(str(min(sizes)))
#print(str(alpha_list_lower[0]) + str(alpha_list_upper[0]))