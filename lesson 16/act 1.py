#total amount calc

def totalamount(bill, tip):
    total = bill*(1+0.01*tip)
    total1 = round(total, 2)

    print("Please pay $", total1)

totalamount(150,20)