from pickle import NONE


minint = 1
maxint = 100
count = 0

while count < 3:
    userint = int(input("Please enter an integer between 1-100: "))
    if userint < 1 or userint > 100:
        print("You have entered an invalid integer")
        count = count + 1
        if count == 4:
            print(NONE)
    else:
        print("Your integer is :" , + userint)
        break
