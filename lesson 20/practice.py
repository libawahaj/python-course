#calender

from datetime import datetime

dt= datetime.now()

print("The current date and time is", dt)

import calendar

yy= 2024
mm= 10

print(calendar.month(yy, mm))
print(calendar.iterweekdays())