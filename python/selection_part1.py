person = int(input("Enter your age: "))

"""
if person >= 18:
	print("You are in category A")

if person >= 16:
	print("You are in category B")

if person < 16:
	print("You are in category C")
"""

if person >= 18:
	print("You are in category A")
elif person >= 16:
	print("You are in category B")
else:
	print("You are in category C")