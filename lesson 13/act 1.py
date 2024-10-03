print("Half pyramid of stars: ")
n = int(input("Enter the number of rows you want: "))
print(n)

for i in range(n):
    for j in range(i+1):
        print("*", end= " ")
    print()
