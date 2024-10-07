#calculator

def add(P,Q):
   return P + Q

def subtract(P,Q):
    return P - Q

def mul(P,Q):
    return P * Q

def divide(P, Q):
    return P/Q

print("Choose what operation you want to do: ")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")

chosen_option = input("Enter your answer as either a, b, c or d: ")

num_1= int(input("Enter the first number: "))
num_2= int(input("Enter the second number: "))

if chosen_option == "a":
    print(num_1 ," + ", num_2, " = ", add(num_1,num_2))

elif chosen_option == "b":
    print(num_1 ," - ", num_2, " = ", subtract(num_1,num_2))

elif chosen_option == "c":
    print(num_1 ," x ", num_2, " = ", mul(num_1,num_2))

elif chosen_option == "d":
    print(num_1 ," / ", num_2, " = ", divide(num_1,num_2))

else: 
    print("Invalid option!")