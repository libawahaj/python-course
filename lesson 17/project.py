def amountdue(a,b):
    return b - a

def amount_to_be_paid(c,d):
    return c - d

bill = int(input("Enter the total bill : "))
amountpaid = int(input("Enter the amount you have paid: "))

if bill < amountpaid:
    money= amountdue(bill,amountpaid)
    print("The amount due to the customer is ", money)

elif bill > amountpaid:
    money2 = amount_to_be_paid(bill,amountpaid)
    print("The customer still has to pay ", money2," more")

else:
    print("The full bill has been paid. No amount is due to the customer.")
