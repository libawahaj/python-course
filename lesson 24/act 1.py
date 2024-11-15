#set of integers

set1 = {1,2,3}
print(set1)

#set of mixed datatypes

set2 = {1.0, "Hello", (1,2,3)}
print(set2)

#removing duplicates in a set

set3 = {1, 2, 3, 2, 4, 5, 3, 3}
print(set3)

#converting a list to a set

set4 = set([1,2,3,4,5])
print(set4)

#remove an element from a set

set5 = {1,2,3,4,5,6,7}
print("The og set is ", set5)
removed = set5.pop()
print("After removing the first element it is: ", set5)