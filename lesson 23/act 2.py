#checking frequency

dict1 = {'First': 2, 'Second': 3, 'Third': 2, 'Fourth': 2}

print("The original dictionary is: ", dict1)

K = 2
count = 0

for key in dict1:
    if dict1[key] == K:
        count = count + 1

print("The number 2 appears ", count, " times.")