# Logical operators
# Python Pizza
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extraCheese = input("Do you want extra cheese? Y or N: ").upper()
finalPrice = 0
if size == 'S':
    finalPrice += 15
elif size == 'M':
    finalPrice += 20
elif size == 'L':
    finalPrice += 25
else:
    print("Wrong Input")
if pepperoni == 'Y':
    if size == 'S':
        finalPrice += 2
    elif size in ('M', 'L'):
        finalPrice += 3
if extraCheese == 'Y':
    finalPrice += 1
print(f"You final bill is: ${finalPrice}")
