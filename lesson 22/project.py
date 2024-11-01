
def multiplication(tuple):
    multipled = 1

    for i in tuple:
        multipled = multipled * i

    return multipled
    

tup1 = (4,3,2,2,-1,18)
print("\n Tuple 1 is : ", tup1)
print("The elements in this tuple multipled give the value: ", multiplication(tup1))

tup2 = (2,4,8,8,3,2,9)
print("\n Tuple 2 is : ", tup2)
print("The elements in this tuple multipled give the value: ", multiplication(tup2), "\n")



