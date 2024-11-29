class Dogs:

    def __init__(self, name, personality, life_expectancy):
        self.name = name
        self.personality = personality
        self.life_expectancy = life_expectancy

    def details(self):
        print(self.name," are ", self.personality, " and are expected to live for about ", self.life_expectancy)

breed1 = Dogs("Miniature poodles", "courageous, confident, smart","10-18 years")
breed2 = Dogs("German Shepherds","active, proud, very smart", "12-14 years")

breed1.details()
breed2.details()