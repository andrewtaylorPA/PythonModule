print("       Pythagoras Calculator")
print("1. Find the length of A given B and C ")
print("2. Find the length of B given A and C ")
print("3. Find the length of C given A and B ")
selection = int(input("Please selection an operation: "))

if selection == 1:
    number1 = int(input("Please enter the length of side B"))
    number2 = int(input("Please enter the length of side C"))
    number3 = number1

elif selection == 2:
    number1 = int(input("Please enter the length of side A"))
    number2 = int(input("Please enter the length of side C"))

elif selection == 3:
    number1 = int(input("Please enter the length of side A"))
    number2 = int(input("Please enter the length of side B"))