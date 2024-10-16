#program to check if the user is a teenager 

try: 
    age = input("Enter your age: ")

    if age < 13:
        print("You are not a teenager.")

    else: 
        print("You are a teenager.")
    
    raise TypeError

except TypeError:
    print("You cannot compare a Str value with an Int value.")


finally:
    print("Code completed successfully.")
