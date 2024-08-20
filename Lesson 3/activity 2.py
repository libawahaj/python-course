amount = int(input("Please enter the amount for withdraw:"))

note1= amount//100
note2= (amount%100)//50
note3= ((amount%100)%50)//10

print("Notes of 100 rupees: ", note1)
print("Notes of 50 rupees: ", note2)
print("Notes of 10 rupees: ", note3)