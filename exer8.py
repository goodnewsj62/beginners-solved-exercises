try:
    inp = input("Enter the name of the file: ")
    file = open(inp, 'r')
except:
    print('Error! wrong input')
    exit()

dic = dict()


for lines in file:
    lines = lines.casefold()
    if lines.startswith('from'):
        lines = lines.rstrip()
        words = lines.split()
        if words[-1].isdigit():
           dic[words[2]] = dic.get(words[2], 0) + 1

print('\tCOUNT OF THE DAYS EACH MAIL WAS SENT')
arr = list(dic.keys())
arr.sort()
for key in arr:
    print(key,dic[key])
