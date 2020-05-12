try:
    inp = input("Enter the file.extention: ")
    file = open(inp, 'r')



    dictionary = dict()
    val = 0
    main_key = ' '

    for line in file:
        if line. startswith('From'):
            line = line.rstrip()
            words = line.split()
            if words[-1].isdigit():
                dictionary[words[1]] = dictionary.get(words[1], 0) + 1

    li = list()

    for key,value in list(dictionary.items()):
        li.append((value,key))
    li.sort(reverse=True)

    for value, key in li[ :1]:
        print(key,value)
except:
    print('Error! you entered the wrong input')