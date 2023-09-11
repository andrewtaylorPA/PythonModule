number1 = int(input("Please enter your first number: "))
number2 = int(input("Please enter your second number: "))

print("1. Add +")
print("2. Subtract - ")
print("3. Multiply * ")
print("4. Divide / ")
print("5. Square s ")

selection = int(input("Please select a number from the above operations: "))

if selection == 1:
    sum = number1 + number2

elif selection == 2:
    sum = number1 - number2

elif selection == 3:
    sum = number1 * number2

elif selection == 4:
    sum = number1 / number2

elif selection == 5:
    sum = number1 ** number2

print("The sum is:", sum)