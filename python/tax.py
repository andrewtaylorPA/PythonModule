
def getIncomeTax(salary):
    pass
    if salary in range(personalallowence):
        print("Your total income tax is: ", incometaxtotal)

    if salary in range(personalallowence, bracket1):
        incometaxable = salary - personalallowence
        incometaxtotal20 = incometaxable * tax1
        print("Your income tax to pay at 20% is: ", incometaxtotal20)
    
    if salary in range(bracket1, bracket2):
        incometaxtotal20 = bracket1allowence * tax1

        incometaxtotal40 = (salary - personalallowence - bracket1allowence) * tax2

        incometaxtotal = incometaxtotal20 + incometaxtotal40
        print(incometaxtotal20)
        print(incometaxtotal40)
        print("Your income tax to pay at 40% is: ", incometaxtotal)

    if salary not in range(bracket2):
        incometaxtotal20 = bracket1allowence * tax1

        incometaxtotal40 = (salary - personalallowence - bracket1allowence) * tax2
        incometaxtotal45 = (salary - personalallowence - bracket1allowence - bracket2allowence) * tax3

        incometaxtotal = incometaxtotal20 + incometaxtotal40 + incometaxtotal45

        print("20$%", incometaxtotal20)
        print("40$%", incometaxtotal40)
        print("45$%", incometaxtotal45)
        print("Your income tax to pay at 45% is: ", incometaxtotal)

personalallowence = 11850

bracket1allowence = 22650
bracket1 = personalallowence + bracket1allowence

bracket2allowence = 115499
bracket2 = bracket1 + bracket2allowence


tax1 = 0.2
tax2 = 0.4
tax3 = 0.45
incometaxtotal = 0

salary = int(input("Please enter your salary: "))

getIncomeTax(salary)