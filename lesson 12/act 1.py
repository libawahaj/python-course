string = input("Enter any word: ")
print("Word is " ,string)

char = input("Enter the character you want to search in the entered word: ")
print("Character is ", char)

i = 0
count= 0
print("Length of the word is ", len(string))

while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1 
print("The total count of ", char, " is " , count)