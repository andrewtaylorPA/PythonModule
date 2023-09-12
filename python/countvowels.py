string = str(input("Please enter a word: "))
vowelcount = 0

for letter in string:
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u":
        vowelcount = vowelcount + 1

print(vowelcount)