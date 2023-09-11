exammark = int(input("Please enter the mark: "))
studentlevel = int(input("Please enter the students level: "))

if exammark < 1 or exammark > 100:
    print("You have entered an incorrect mark, please enter between 1-100")
else:
    if studentlevel == 1:
        print("Student is level 1")
        if exammark < 50:
            print("Fail")
        elif exammark >= 50 and exammark <= 60:
            print("Pass")
        elif exammark >= 61 and exammark <= 70:
            print("Merit")
        elif exammark >= 71 and exammark <= 100:
            print("Distinction")

    elif studentlevel == 2:
        print("Student is level 2")
        if exammark < 40:
            print("Fail")
        elif exammark >= 40 and exammark <= 50:
            print("Pass")
        elif exammark >= 51 and exammark <= 65:
            print("Merit")
        elif exammark >= 66 and exammark <= 100:
            print("Distinction")