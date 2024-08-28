#identity 

x = 5

if (type(x) is int):
    print( x, " is an integer")

else:
    print(x, " is not an integer")


y = 5.5

if (type(y) is not int):
    print(y, " is not an integer")

else:
    print(y, "is a float")

#membership

text = "My name is liba"
search_text = "liba S"

if search_text in text:
    print("search found")

elif search_text not in text:
    print("search not found")