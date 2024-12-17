class Pakistan:

    def capital(self):
        print("The capital of Pakistan is Islamabad.")

    def language(self):
        print("The mother tongue of Pakistan is Urdu.")

    def type(self):
        print("Pakistan is a developing country.")

class UAE:

    def capital(self):
        print("The capital of the UAE is Abu Dhabi.")

    def language(self):
        print("The mother tongue of the UAE is Arabic.")

    def type(self):
        print("The UAE is a developed country.")

obj_pak = Pakistan()
obj_UAE = UAE()

for country in (obj_pak,obj_UAE):
    country.capital()
    country.language()
    country.type()