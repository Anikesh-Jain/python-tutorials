import random

def play_game():
    print("Welcome to the Guess Game")
    lucky_num = random.randint(1, 50)
    print("Guess the lucky Number to win")

    while True:
        user_num = int(input("Guess the lucky number: "))

        if user_num == lucky_num:
            print("Congratulations!, You Guessed the Correct Number")
            print("The Lucky Number was : ", lucky_num)
            break
        elif user_num < lucky_num:
            print("Your Number is too small")
        else:
            print("Your Number is too High")

    print("Game Clear!, Thank you for playing.")

play_game()