import random
from Hangman_words import word_list
from Hangman_art import logo, stages

chosen_word = list(random.choice(word_list))
size_word = len(chosen_word)
available_tries = 6

print(logo)

placeholder = ["_" for i in range(size_word)]
print("".join(placeholder))
game_over = False

while not game_over:

    print(f"****************************{available_tries}/6 LIVES LEFT****************************")
    guess = input("Guess a letter:\n").lower()

    if guess in placeholder:
        print(f"{guess} has already guessed")
        continue

    for ind, item in enumerate(chosen_word):
        if guess == item:
            placeholder[ind] = item


    print("".join(placeholder))

    if guess not in placeholder:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        available_tries -= 1
        if available_tries == 0:
            game_over = True
            print(f"{"".join(chosen_word)} is guessed word")
            print(f"***********************YOU LOSE**********************")

    if "_" not in placeholder:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[available_tries])



