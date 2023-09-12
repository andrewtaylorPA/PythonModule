# While loops1

testvar = 1

while testvar < 5:
    print("Hello World!")
    testvar = testvar + 1

inputvar = int(input("Enter a number"))
while inputvar < 20:
    print(inputvar)
    inputvar = inputvar + 1

inputvar = int(input("Enter a number"))
while inputvar < 0:
    print(inputvar)
    inputvar = inputvar - 1

inputvar = int(input("Enter a number"))
while inputvar < 20:
    if inputvar == 13:
        break
    print(inputvar)
    inputvar = inputvar + 1


