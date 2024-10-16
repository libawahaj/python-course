#asking age and seeing if its even or odd

try:
    age = int(input("Enter your age: "))
    
    def correct_age(a):
        if 13 <= a < 18:
            print("You are a teenager.")
        elif a < 13:
            print("You are a child.")
        else:
            print("You are an adult.")
    
    correct_age(age)

    def even_or_odd(b):
        if b % 2 == 0:
            print("Your age is an even number.")
        else:
            print("Your age is an odd number.")
    
    even_or_odd(age)

except ValueError as ex:
    print("Exception:", ex)