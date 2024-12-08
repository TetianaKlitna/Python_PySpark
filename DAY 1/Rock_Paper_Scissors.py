import random

items = ["Rock", "Paper", "Scissors"]
print("What do you choose?")
yourChoose = int(input("Type 0 for Rock, 1 for Paper, or 2 for Scissors "))
computerChoose = random.randint(0, 2)
print(f"Computer choose: {items[computerChoose]}")

if yourChoose not in [0, 1, 2]:
    print("Input error")
else:
    if yourChoose ==  computerChoose:
        print("No one has win.")
    elif yourChoose == 0 and computerChoose == 2 or yourChoose == 2 and computerChoose == 1 or yourChoose == 1 and computerChoose == 0:
        print("You win")
    elif yourChoose == 2 and computerChoose == 0 or yourChoose == 1 and computerChoose == 2 or yourChoose == 0 and computerChoose == 1:
        print("You lose")
