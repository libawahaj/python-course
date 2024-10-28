#making a list of words that have the same first and last letter

def matchingWords(words):
    list1 = []
    character = 0
    for word in words:
        if len(words) > 1 and word[0] == word[-1]:
            character += 1
            list1.append(word)

    print("The list of words that have the same first and last letter are: ", list1)
    return character

count = matchingWords(["aba", "abc", "dog", "gog"])
print("The total count is ", count)