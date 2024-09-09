n = int(input("Enter the number whose table you want to generate: "))
b = int(input("Enter the maximum range you want the table to generate: "))

for a in range(1,b+1):
    print( n , " x ", a, " = ", n*a)