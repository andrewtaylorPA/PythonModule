
scoremath = int(input("Math mark: "))
for x in range(100000000):
    if scoremath < 1 or scoremath > 100:
        scoremath = int(input("Invalid mark, please enter a valid Math mark: "))
    else:
        print("Input valid")
        break

scoreenglish = int(input("English mark: "))
for x in range(100000000):
    if scoreenglish < 1 or scoreenglish > 100:
        scoreenglish = int(input("Invalid mark, please enter a valid English mark: "))
    else:
        print("Input valid")
        break

scoreict = int(input("ICT mark: "))
for x in range(100000000):
    if scoreict < 1 or scoreict > 100:
        scoreict = int(input("Invalid mark, please enter a valid ICT mark: "))
    else:
        print("Input valid")
        break

averagemark = (scoremath + scoreenglish + scoreict) / 3

print("Math mark is:", +scoremath)
print("English mark is:", +scoreenglish)
print("ICT mark is:", +scoreict)
print("Average mark is:", averagemark)

if averagemark >= 65:
    print("This is a pass!")
elif averagemark > 65:
    print("This is a fail")

 