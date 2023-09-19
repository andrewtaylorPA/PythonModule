## If statement exercises

# E34 - Odds or evens

def OddorEven():

    integer = int(input("Please enter an integer: "))

    if (integer % 2) == 0:
        print(integer, "is even")
    else:
        print(integer, "is odd")


# E35 Dog Years
def DogYears():

    dogage = float(input("How old is your dog in years?: "))
    dogageconverted = 0

    if dogage <= 0:
        print("Pleas enter a valid age")
    elif dogage < 3:
        dogageconverted = dogage * 10.5
    else:
        dogagecurve = dogage - 2
        dogagecurve = dogagecurve * 4
        dogageconverted = dogagecurve + 21
    print("Dog age in dog years is: ", dogageconverted)


# E104 Sorted Order

def SortOrder():
    
    integers = []
    integer = 1
    
    while integer != 0:
        integer = int(input("Pleas enter an integer: "))
        integers.append(integer)

    integers.sort()
    for integer in integers:
        print(integer)


# E

#SortOrder()
#OddorEven()
#DogYears()
