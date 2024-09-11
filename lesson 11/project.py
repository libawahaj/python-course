num1 = input("Enter any number: ")
length= 0 

length = len(num1)

print("The number of digits in ", num1, " is ", length)

#second method

num2 = int(num1)
length= 0 

while num2 != 0:
    num2 //= 10
    length += 1 

print("The number of digits in ", num1 , " is ", length)