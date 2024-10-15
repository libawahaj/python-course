num = int(input("Enter the decimal number you want to convert to binary: "))
print("The number is ", num)
remainder = 0
b = ""
n = num

while n > 0:
    remainder = n%2
    b = str(remainder) + b
    n = n//2
    
print(b, " is the binary of ", num)
    






         
        

