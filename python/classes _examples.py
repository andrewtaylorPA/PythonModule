## Classes

# A Programatic object containing data and methods
# ie variable and functions

# basic form
"""
class Classname:

    attribute = "some data"

    def methodname(input):
        <code for method>
        return value

"""

class Dog:
    
    breed = "labrador"
    weight = 35
    energy = "High"

    def communicate(self):
        return "Woof"

goldie = Dog()

print(goldie.breed)
print(goldie.communicate())
print(goldie.energy)

bonnie = Dog()
bonnie.energy = "Medium"

print(bonnie.breed)
print(bonnie.communicate())
print(bonnie.energy)