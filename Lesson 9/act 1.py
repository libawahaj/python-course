med = input("Do you have any history of medical problems? Answer with Y for yes or N for no:")
attend = int(input("Enter your attendance percentage:"))

if med == "Y":
    print("You are allowed to take the exam.")

else:
    if attend >= 75:
        print("You are allowed to take the exam.")

    else:
        print("You are not allowed to take the exam.")