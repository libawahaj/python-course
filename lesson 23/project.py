#test dictionary 

test_dict = {'Codingal' : 3, 'is' : 2, 'best' : 2, 'for': 2, 'Coding' : 1}

print("The original dictionary is: ", test_dict)
K = int(input("Enter the number whose frequency you want to check: "))

count = 0

for key in test_dict:
    if test_dict[key] == K:
        count = count + 1

print("The number ", K, " appears ", count, " times in this dictionary.")


#user inputted

user_dict = {}
n = int(input("Enter number of students whose scores you want to record: "))
for i in range (0, n):
    key = input("Enter the name of the student: ")
    value = int(input("Enter the score of this student out of 10: "))
    user_dict[key] = value

print("\nThe student's scores out of 10 are as follows: ", user_dict)

A = int(input("Enter the score whose frequency you would like to find: "))

count2 = 0

for key in user_dict:
    if user_dict[key] == A:
        count2 = count2 + 1

print("The score ", A, " appears ", count2, " times among the students.")