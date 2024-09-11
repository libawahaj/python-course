n = int(input("Enter the value of the terms: "))

sum= 0
i = 1

while i <= n:
    sum = i + sum
    i = i + 1

print("The sum of ", n, " is ", sum)