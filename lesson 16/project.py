#shutdown function

def shutdown(response, response2=None):
    '''Function to shutdown the program'''

    if response == "yes" and response2== "yes":
        print("Program is shutting down.")

    elif response == "no" or response2== "no":
        print("Abort shut down")

    else:
        print("Sorry.")


a = input("Do you want to shut down the program? ").lower()
if a == "yes":
    b = input("All your data will be lost if it is not saved. Do you confirm shutdown? ").lower()
    shutdown(a,b)

else: 
    shutdown(a)

