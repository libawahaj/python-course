#generating random date

import time
import random

def getrandomDate(start, end):
    print("Getting a random date between ", start ," and ", end)
    randomGenerator = random.random()
    dateFormat= "%m/%d/%Y"

    startTime = time.mktime(time.strptime(start, dateFormat))
    endTime = time.mktime(time.strptime(end, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random date: ", getrandomDate("2/7/2023", "8/9/2024"))


