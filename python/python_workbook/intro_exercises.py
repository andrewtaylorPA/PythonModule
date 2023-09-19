## Intro exercises from "The Python Workbook
## Execises 1 - 

#E1 - Mailing List

from cgitb import small
from ctypes.wintypes import FLOAT


name = "Andew Taylor"
addressline1 = "2 River Street"
addressline2 = "Selby"
postcode = "YO8 5AP"
county = "North Yorkshire"

print(name)
print(addressline1)
print(addressline2)
print(postcode)
print(county)

#E2 - Hello

name = (str(input("Please enter your name: ")))
print("Hello", name+ "!")

#E3 - Area of a room

roomLength = (float(input("Please enter the rooms length in meters: ")))
roomWidth = (float(input("Please enter the rooms width in meters: ")))
roomArea = roomLength * roomWidth
print("Room length: ", roomLength, "m")
print("Room width: ", roomWidth, "m")
print("The rooms area is :", roomArea, "m2")

#E4 - Area of a field

fieldLength = (float(input("Please enter the fields length in feet: ")))
fieldWidth = (float(input("Please enter the fields width in feet: ")))
acreSquareFeet = 43560

fieldAcre = (fieldLength * fieldWidth) / acreSquareFeet
print("The field is :", fieldAcre, "acres")

#E5 - Bottle deposits

smallDeposit = 0.1
bigDeposit = 0.25

smallBottle = float(input("How many bottles 1 ltr or under?: "))
bigBottle = float(input("How many bottles over 1 ltr?: "))

smallRefund = smallBottle * smallDeposit
bigRefund = bigBottle * bigDeposit
print("Refund amount - Small Bottles: $",(round(smallRefund,2)))
print("Refund amount - Big Bottles: $",(round(bigRefund,2)))

#E6 - Tax and Tip

tax = 0.20 # 20%
tip = 0.18 # 18%

mealcost = float(input("Meal cost: "))
mealtax = mealcost * tax
mealtip = mealcost * tip
mealtotal = mealcost + mealtip + mealtax

print("Tip is: ", round(mealtip,2))
print("Tax is: ", round(mealtax,2))
print("Total meal: ", round(mealtotal,2) )

#E7 - Sum of the first n integers
total = 0
integer = int(input("Enter an integer: "))

for number in range (1,integer + 1):
    total = total + number
print("The sum of the integers is: ", total)

#E8 - Widgets and Gizmos

widgetWeight = 75
gizmoWeight = 112

widgets = int(input("How many widgets in the order?: "))
gizmos = int(input("How many gizmos in the order?: "))

widgetTotalWeight = widgetWeight * widgets
gizmoTotalWeight = gizmoWeight * gizmos

orderTotalWeight = widgetTotalWeight + gizmoTotalWeight

print("Order total weight is: ", orderTotalWeight, "grams")


