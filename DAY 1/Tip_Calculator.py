#Data Types
#Tip Calculator
print("Welcome to the tip calculator!")
totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("How much tip would you like give? 10, 12, or 15 "))
amountPeople = int(input("How many people to split the bill? "))
pay = round(totalBill*(1 + tipPercent/100)/amountPeople, 2)
print(f"Each person should pay: ${pay}")