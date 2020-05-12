print("End program by entering \"done\"")
hold = list()

while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        print('Maximum: ', max(hold))
        print("Minimum: ",  min(hold))
        break
    hold.append(inp)

