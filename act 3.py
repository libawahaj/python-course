mean1 = 38
wrong_number = 36
correct_number = 56
total_number = 40

#sum of 40 numbers
sum = mean1 * total_number
print("The sum of 40 numbers: ", sum)

#correct sum after adjusting for the wrong number
num2 = sum - wrong_number + correct_number
print("Corrected sum: ", num2)

#correct mean
mean2 = num2 / total_number
print("The corrected mean: ", mean2)