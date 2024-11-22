#1. Take a number from the user, create a list with all the odd numbers under the input value and another list of odd numbers.

#user input

numbers = []
n = int(input("Enter number of elements: "))
for i in range (0, n):
    num = int(input("Enter one of the numbers in your list: "))
    numbers.append(num)

oddNumbers = [x for x in numbers if x%2==1]
print("The list of odd numbers entered are ",oddNumbers)

#2. Create a list of fruits. Then, convert the first letter of every element to capital and create a new list of updated values.

fruits = ['apples', 'oranges', 'bananas']

capitalized = [fruit.capitalize() for fruit in fruits]

print(capitalized)