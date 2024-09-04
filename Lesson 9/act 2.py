units = int(input("Enter the number of units you've consumed: "))

if units <= 50:
    amount = units * 2.60
    surcharge = 25

elif units > 50 and units <= 100:
    amount = 130 + ((units - 50) * 3.25)
    surcharge = 35

elif units > 100 and units <= 200:
    amount = 130 + 162.50 + ((units - 100) * 5.26)
    surcharge = 45

else: 
    amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surcharge = 75

total_amount = amount + surcharge

print("Your electricity bill is ", total_amount)