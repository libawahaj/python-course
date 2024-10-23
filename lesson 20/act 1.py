#datetime module

from datetime import datetime, time, date

td = date.today()
ct = datetime.now()

print("The date today is ", td)
print("The current date and time right now is ", ct)

print("Components of data: ", td.year, td.month, td.day)