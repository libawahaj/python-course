#finding factorials
#0!= 1 and 1!= 1, 3!= 3 x 2 x 1
 
def factorial(x):
    '''Finding the factorial of a number using recursive function '''
    #recursive function is the function that calls itself 

    if x == 0 or x == 1:
        return 1
    
    else:
        return x*factorial(x-1)
    
print(factorial.__doc__)
a = int(input("Enter any number: "))

print("The factorial of ", a, " is ", factorial(a))