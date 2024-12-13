print("Welcome to Treasure Island.\nYour mission is to find the treasure")
print("You're at a cross road. Where do you want to go?")
direction = input("Type \"left\" or \"right\" ").strip().lower()
if direction == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    action = input(
        "Type \"wait\" to wait for a boat. Type \"swim\" to swim across. ").strip().lower()
    if action == "wait":
        color = input("Which door? red, yellow, or blue ").strip().lower()
        if color == "yellow":
            print("You win!")
        else:
            print("Game over.")
    else:
        print("Game over.")
else:
    print("Game Over.")
