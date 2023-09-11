#Selection examples

inputvar = int(input('Input a number that is not 7:'))

if inputvar == 7:
    print("You typed 7 even though I said not to")

if inputvar > 7:
    print("You typed a big number")

if inputvar != 7:
    print("This number is not 7")

    # == is equal to
    # = add value to variable


if inputvar > 7 and inputvar < 1000:
    print("Your number is between 8 and 999")

if inputvar ==7 or (inputvar > 12 and inputvar < 20):
    print("Either 7 or in the teens")

if inputvar > 10:
    print("You passed")
else:
    print("You failed")

    #Using elif to perform multiple sequential tests

if inputvar < 10:
    print("You have a single digit number")
elif inputvar < 100:
    print("You have a double digit number")
elif inputvar < 1000:
    print("You have a triple digit number")
else:
    print("Your number is huge")

    # Nested If statement
if inputvar < 1000:
    if inputvar < 100:
        if inputvar < 10:
            print("You have a one digit number")
        else:
            print("You have a two digit number")
    else:
        print("You have a three digit number")
else:
    print("Your number is huge")


