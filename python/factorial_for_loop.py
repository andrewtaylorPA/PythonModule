inputvar = int(input("Enter an integer: "))
factorial = 1
for number in range(1,inputvar + 1):
    factorial = factorial * number
print("The factorial of" ,number,"is",factorial)