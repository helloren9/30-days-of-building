import random

def play_game():
    choice = input("Choose difficulty (easy/medium/hard): ").lower()
    if choice == 'easy':
        max_tries = 10
    elif choice == 'medium':
        max_tries = 7
    elif choice == 'hard':
        max_tries = 5
    else:
        print("Invalid choice. Exiting game.")
        exit()

    print(f"--- {choice.upper()} Game Started! ---")
    num = random.randint(1, 20)
    guesses_left = max_tries

    print(f"I am thinking of a number between 1 and 20. You have {guesses_left} chances to guess it.")

    while guesses_left > 0:
        try:
            guess = int(input(f"Enter your guess: "))
        except ValueError:
            print("Please guess a NUMBER: ")
            continue

        if guess == num:
            print("You got it. Amazing!")
            break
        elif guess > num:
            print("Too high.")
        elif guess < num:
            print("Too low.")

        if abs(guess - num) <= 3 and guess != num:
            print("You are getting very close!")

        guesses_left -= 1
        print(f"Guesses left: {guesses_left}")

    if guesses_left == 0:
            print(f"Sorry, you ran out of guesses. The number was {num}. Better luck next time!")

while True:
    play_game()
    restart = input("Play again? (y/n): ").lower()
    if restart != 'y':
        print("Thanks for playing!")
        break