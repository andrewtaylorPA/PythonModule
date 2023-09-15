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

class Budget:

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

Food_budget = Budget(300,"Food")
Food_budget.display()
Food_budget.deposit()
Food_budget.withdraw()


Shopping_budget = Budget(1000,"Shopping")
Shopping_budget.display()
Shopping_budget.deposit()
Shopping_budget.withdraw()

transferfood = int(input("How much to transfer to shopping budget?: "))

Food_budget.transfer(Shopping_budget,transferfood)

transfershopping = int(input("How much to transfer to food budget?: "))

Shopping_budget.transfer(Food_budget,transfershopping)


