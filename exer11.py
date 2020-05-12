
file = open(r'C:\Users\Goodnews\Downloads\38 Amazing Open Source Android Apps written in Java_files\mbox-short.txt', 'r')
dic = dict()

for line in file:
    line = line.rstrip()
    hold = tuple(line)
    for each in hold:
        if each.isalpha():
            dic[each] = dic.get(each, 0) + 1

li = list()
for fir,sec in list(dic.items()):
    li.append((sec,fir))

li.sort(reverse = True)

for x,y in li:
    print(x,y)
