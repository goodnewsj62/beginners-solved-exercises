rOpen = open('romeo.txt', 'r')
new = list()
hold = False

for lines in  rOpen:
    lines = lines.rstrip()
    words = lines.split()
    for i in range(len(words)):
        for j in range(len(new)):
            if words[i] == new[j]:
                hold = True
        if hold == False:
            new.append(words[i])
        hold = False


new.sort()
print(new)

