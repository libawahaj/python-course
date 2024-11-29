class Dogs:

    group = "Herding group dogs: " #one class variable

    def __init__(self, name, personality): #two instance variables
        self.name = name
        self.personality = personality

    def details(self):
        print(self.name," are ", self.personality)

breed1 = Dogs("Australian Cattle Dogs", "loyal, intelligent, and tenacious")
breed2 = Dogs("German Shepherds","active, proud, and very smart")

print(Dogs.group)
breed1.details()
breed2.details()