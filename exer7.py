fwords = open(r'C:\Users\Goodnews\Downloads\38 Amazing Open Source Android Apps written in Java_files\words.txt', 'r')
hold = dict()

for list in fwords:
    list = list.rstrip()
    words = list.split()
    for word in words:
        hold[word] = ' '

print(hold)
print(('making' in hold))