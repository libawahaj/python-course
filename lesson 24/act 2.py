#intersection and union function

set1 = {'yellow', 'blue'}
set2 = {'green', 'blue'}

print("The original elements in a set are: ")
print(set1)
print(set2)

print("The intersection between the two sets are: ")

set3 = set1.intersection(set2)
print(set3)

print("The union between the two sets are: ")

set4 = set1.union(set2)
print(set4)

#difference function

print("The difference between the two sets are: ")
set5_difference = set1.difference(set2)
print(set5_difference)

#symmetric difference

print("The symmetric difference between the two sets are: ")
set_symmetricDifference = set1.symmetric_difference(set2)
print(set_symmetricDifference)