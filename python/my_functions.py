# User created functions

def functionName():
    #code here
    pass # this pass keyword lets you define a function without code

def showTwo(): # this defines function
    print(2)

showTwo() # This calls function to run it

def addTwo(inputvar):
    if inputvar.isnumeric():
        print(int(inputvar + 2))
    else:
        print("You didn't give me a number")

mynumber = input("Number: ")

addTwo(mynumber)

