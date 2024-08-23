character = input("Enter any character: ")

if len(character) == 1 and character.isalpha():
    print(character, "is an alphabet.")

else:
    print(character, "is not an alphabet")