#number guessing game

import random 

playing = True
user_num = int(input("Guess any number between 0 and 10: "))

number = random.randint(0,10)

while playing:
    if user_num == number:
        print("You've guessed the number!")
        break

    else:
        print("You've got it incorrect! Try again.")
        break

print("The correct number is ", number)