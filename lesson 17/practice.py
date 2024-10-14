#keywords

#return

def r(a,b):
    c = a + b
    return c 

r(5,10)

#continue

def continued():
    for i in range(9):
        if i == 3:
            continue
        print(i)

continued()

#break

def break1():
    for j in range(5):
        if j == 2:
            break
        print(j)

break1()

#pass

def pass1(a,b):
    if a > b:
        pass

    else: 
        print("b is greater than a ")

pass1(3,4)