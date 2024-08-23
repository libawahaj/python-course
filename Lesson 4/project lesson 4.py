cost = float(input("Enter the cost of the product you wish to buy: "))

day = input("Enter the day on which you're buying this product: ").lower()

if day in ["saturday", "sunday"]:
    discounted = cost*0.8
    print("You got a weekend discount of 20% off! Your new cost is", discounted)

else:
    print("You have gotten no discount. The cost of the product is still", cost)

#Temperature project
light_clothes_temp = 20
current_temp = float(input("Enter the current temperature in celsius: "))

if current_temp >= light_clothes_temp:
    print("You can wear light and soft clothes.")
else:
    print("It's too cold for light clothes. Wear something warmer.")