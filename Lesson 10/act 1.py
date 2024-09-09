n = int(input("Enter the total numbers whose sum you want to find out: "))
sum = 0

for i in range(1, n+1):
    sum = sum + i
    print("Sum = ", sum)