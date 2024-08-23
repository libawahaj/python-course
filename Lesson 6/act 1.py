#AND operator

a = 20
b = 40

if a < 0 and b > 0:
    print(a , " and ", b , " are greater than 0.")

else:
    print(a , " and ", b , " are lesser than 0.")

#OR operator

c = 10
d = 5

if c > 0 or d == 0:
    print("Either one of the numbers are greater than 0")

else: 
    print("The numbers are lesser than 0")

#NOT operator

e = 6

if not e:
    print("The answer is ", e)

else:
    print("The answer is not ", e)