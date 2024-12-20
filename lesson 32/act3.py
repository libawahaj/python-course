import random

class FruitsQuiz:

    def __init__(self):

        self.fruits = {"apple": "red", "orange": "orange", "banana": "yellow", "grapes": "green"}

    def quiz(self):

        while True:
           
            fruit, colour = random.choice(list(self.fruits.items()))

            print("What is the colour of", fruit, "?")
            answer = input("Enter your answer here: ")

            if answer.lower() == colour:
                print("Your answer is correct. Congrats!")
            else:
                print("Your answer is incorrect. The correct answer is", colour)

            option = int(input("Enter 0 if you want to end the game, or 1 to replay: "))

            if option == 0:
                print("Game has ended. Thanks for playing!")
                break  

            elif option == 1:
                print("Let's play again!\n")

            else:
                print("Invalid option. Ending the game.")
                break 

print("Welcome to the fruit quiz!")
fq = FruitsQuiz()
fq.quiz()