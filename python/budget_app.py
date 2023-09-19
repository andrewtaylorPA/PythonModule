## budget app

"""
class budget:
    def deposit(self):
        pass
    def withdraw(self):
        pass

food = budget()
clothing = budget()
"""

# Class defines default attributes for a method

class Budget:

    # this __init__ method initialises the variables needed for the class - note these can be static values
    def __init__(self,passedbudget,passedcategory):
        self.budget = passedbudget
        self.category = passedcategory

    def deposit(self):
        self.deposit = (int(input("How much would you like to input?: ")))
        self.budget = self.budget + self.deposit
        self.display()

    def withdraw(self):
        self.withdraw = (int(input("How much would you like to withdraw?: ")))
        self.budget = self.budget - self.withdraw
        self.display()

    def display(self):
        print("Your total funds in {} are: {}".format(self.category,self.budget))

    def transfer(self,transfercategory,transferamount):
        transfercategory.budget = transfercategory.budget + transferamount
        self.budget = self.budget - transferamount
        self.display()
        transfercategory.budget

#class called into a variable with the parameters 300 and food which relate to the budget and the category

Food_budget = Budget(300,"Food") # So this creates an instance of budgety which has the food category and value of 300
Food_budget.display()
Food_budget.deposit() # This runs the deposit method in the class
Food_budget.withdraw()


Shopping_budget = Budget(1000,"Shopping")
Shopping_budget.display()
Shopping_budget.deposit()
Shopping_budget.withdraw()

transferfood = int(input("How much to transfer to shopping budget?: "))

Food_budget.transfer(Shopping_budget,transferfood) # This runs the food_budget instance of the budget class, passing in 2 variables that the method needs

transfershopping = int(input("How much to transfer to food budget?: "))

Shopping_budget.transfer(Food_budget,transfershopping)


