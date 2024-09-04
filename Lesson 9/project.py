age = int(input("Enter the student's age: "))

if age >= 10:
    if age <= 20:
        print("The student is able to enroll in the class.")
    else:
        print("The student cannot enroll in the class because they are older than 20")
else:
    print("The student cannot enroll in the class because they are younger than 10")