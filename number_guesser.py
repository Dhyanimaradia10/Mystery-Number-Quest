# Made By: Dhyani Maradia

import random

print("Number Guesser")

while True:
    print("Give the range to predict the number in between that range.")
    starting_index = int(input('Starting from number: '))
    ending_index = int(input('to the number: '))
    print()

    random_number = random.randint(starting_index, ending_index)
    guesses = 0

    while True:
        guesses+=1
        user_input = int(input('Make a guess: '))

        if user_input == random_number:
            print("You got it... \n")
            break
        elif user_input>random_number:
            print("Too High \n")
        else:
            print("Too low \n")

    print("You got in ",guesses, " guesses.")

    ans = input("Do you want to play again? (yes/no): ").lower()
    print()
    if ans!='yes':
        print("Thank you for playing, Have a nice day.")
        break
