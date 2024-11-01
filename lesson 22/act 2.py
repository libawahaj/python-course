#palindrome checker

#creating function

def palindrome(r):
    e = len(r) - 1
    s = 0

    while (s<e):
        if (r[s] != r[e]):
            return False
        s = s + 1
        e = e - 1

    return True 

r = (1, 2,3,4,5,6)
print ("The truple is : ", r)

if palindrome(r):
    print("The truple is a palindrome")

else: 
    print("The truple is not a palindrome")

