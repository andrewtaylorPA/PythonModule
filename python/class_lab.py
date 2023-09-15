class Student:

    def __init__(self,passedname,passedage):
        self.name = passedname
        self.age = passedage

    def displaydetails(self):
        print("Name: ", self.name, "and age: ", self.age)

    def getage(self):
        self.age = input("Enter age for " + self.name + ": ")
        self.displaydetails()


student1 = Student("Richard Smith","25")
student2 = Student("Annabelle Chapman","29")

print(student1.displaydetails())
print(student2.getage())