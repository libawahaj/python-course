#half pyramid with numbers

print("Half pyramid of numbers: ")
r = int(input("Enter the number of rows you want: "))
print(r)

for i in range(r):
    for j in range(i+1):
        print(i, end= " ")
    print()
