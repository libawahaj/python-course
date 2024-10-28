#square values of the numbers in a list

numbers = [1, 2, 3, 4, 5]
squaredlist = []

print("The numbers in a list are: ", numbers)

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

