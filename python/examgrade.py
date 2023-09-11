exammark = int(input("Please enter the mark: "))

if exammark < 1 or exammark > 100:
    print("You have entered an incorrect mark, please enter between 1-100")
elif exammark < 50:
    print("Fail")
elif exammark >= 50 and exammark <= 60:
    print("Pass")
elif exammark >= 61 and exammark <= 70:
    print("Merit")
elif exammark >= 71 and exammark <= 100:
    print("Distinction")