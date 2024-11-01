#tuple with various datatypes

tp1 = (1, 2.5, False, "cat")

print(tp1)

#tuple of integers

tp2 = (1, 2, 3, 4, 5)
print(tp2)

tp3 = tp2 + (9,)
print(tp3)

#counting occurences of a certain element

count = tp2.count(5)
print("5 appears ", count, " times.")

#slicing a tuple

print(tp3[2:5])
print(tp3[:4])