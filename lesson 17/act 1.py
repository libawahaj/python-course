
word = input("Enter any word: ")

def wordfinder():
    for i in word: 
        if (i == "A"):
            print("A is found")
            break

        else:
            print("A is not found")

wordfinder()