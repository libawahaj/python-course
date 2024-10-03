print("Floyd's triangle of natural numbers: ")
rows = int(input("Enter the number of rows you want: "))
print(rows)
number = 1 

for i in range(1, rows + 1):
    for columns in range(1, i + 1):
        print(number, end= "   ")
        number = number + 1
    print()
