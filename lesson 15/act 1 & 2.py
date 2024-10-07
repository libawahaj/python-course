#act 1

def well_wishes(): #defining a function
    print("Hello!")
    print("How are you?")

#calling a function
well_wishes()

#act 2

def weather(a,b):
    if a == "spring" and b <= 30:
        print("The weather is nice in ", a)
    
    else: 
        print("The weather is rainy in autumn")
        
print("Choose the weather as either spring or autumn: ")
a = input("Enter the weather you have chosen: ")
b = int(input("Enter the temperature: "))

weather(a,b)