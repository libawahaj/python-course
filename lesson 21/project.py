#user input the list

numbers = []
n = int(input("Enter number of elements: "))
for i in range (0, n):
    num = int(input("Enter one of the numbers in your list: "))
    numbers.append(num)

squaredlist = []

print("The numbers in your list are: ", numbers)

#square values of the numbers in a list

for singleNumber in numbers:
    squared = singleNumber ** 2
    squaredlist.append(squared)

print("The square values for the list of numbers are: ", squaredlist)

#dividing the list into odd and even 

evenList = []
oddList = []

for oddOreven in squaredlist:
    if oddOreven % 2 == 0:
        evenList.append(oddOreven)

    else:
        oddList.append(oddOreven)

print("The even numbers in the list are: ", evenList)
print("The odd numbers in the list are: ", oddList)

