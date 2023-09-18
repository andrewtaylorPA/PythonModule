""" Dice Class

Write a class called Dice
When initialised the object will set how many faces the die has
Create objects for 6, 20, 2 and 4 sided die.
Roll a charactor sheet for a Swashbuckler Rogue called 'Earl Grey' DnD 5th ed. """

import random

class Dice:

    def __init__(self,passedsides):
        self.sides = passedsides

    def roll(self):

        if dice_sides in [2,4,6,20]:

            attributes = ["Strength","Dexerity","Intelect","Agility"]

            for attribute in attributes:
                print(attribute, " : ", random.randint(1,self.sides))
        else:
            print("You have not entered a valid dice")

dice_sides = int(input("How many sides does your dice have?: (2,4,6,20) "))
dice_roll = Dice(dice_sides)
dice_roll.roll()

dice_sides2 = int(input("How many sides does your dice have?: (2,4,6,20) "))
dice_roll2 = Dice(dice_sides2)
dice_roll2.roll()
