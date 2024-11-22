#map function

#with anonymous function (lambda)

list1 = [1,2,3,4]
list2 = [5,6,7,8]

added = map(lambda a,b: a+b,list1, list2)
print(list(added))

#without anonymous function

def cube(x):
    return x*x*x

list3 = [2,3,4]

cubed = map(cube, list3)
print("The list of ", list3, " cubed is ", list(cubed))
