
class Employee:

    def __init__(self):
        print("This is a constructor.")

    def __del__(self):
        print("Class destructed")


def Create_obj():
    print("Function started")
    obj = Employee()
    print("Function ended")

obj1 = Create_obj()