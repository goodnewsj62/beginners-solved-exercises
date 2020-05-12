file = open(r'C:\Users\Goodnews\Downloads\38 Amazing Open Source Android Apps written in Java_files\mbox-short.txt', 'r')

dic = dict()
for line in file:
    if line.startswith('From'):
        line = line.rstrip()
        word = line.split()
        if word[-1].isdigit():
            hold = word[5]
            extract = hold[:2]
            dic[extract] = dic.get(extract, 0) + 1

li = list()


for each in list(dic.items()):
    li.append(each)

li.sort()

for x,y in li:
    print(x,y)

