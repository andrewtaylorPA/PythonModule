initialinvestment = int(input("Please enter an initial investment: "))
targetvalue = int(input("Please enter a target value: "))
interestrate = float(input("Please enter a interest rate as a decimal: "))
yearstaken = 0

while initialinvestment < targetvalue:
    interesttoadd = initialinvestment * interestrate
    initialinvestment = initialinvestment + interesttoadd
    yearstaken = yearstaken + 1
    print(initialinvestment)
    
print("The number of years taken is :", +yearstaken)