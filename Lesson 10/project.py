base = int(input("Enter the base number: "))
exponent = int(input("Enter the power number: "))
n3 = 1


n3= base**exponent
print(base, " to the power of ", exponent, " is ", n3)

#second method
n3= 1

for i in range (1, exponent+1 ):
    n3= n3*base

print(base, " to the power of ", exponent, " is ", n3)