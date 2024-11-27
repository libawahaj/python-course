import random 

def passwordGenerator():
    a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    lower_case = random.choice(a)
    upper_case = random.choice(b)
    number = random.randint(0,100)

    password = lower_case + upper_case + str(number)
    return password

print("Your password is: ", passwordGenerator() + passwordGenerator())