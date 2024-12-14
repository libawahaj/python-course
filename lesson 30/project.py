class Reverse: 
    
    def __init__(self):
        self.s = ""
        
    def inp(self):
        self.s = input("Enter any word: ")
        print("The word you have entered is ", self.s)
        
    def reversed(self):
        reversed_s = self.s[::-1]
        print("The reverse of this string is ", reversed_s)
            
obj = Reverse()
obj.inp()
obj.reversed()

