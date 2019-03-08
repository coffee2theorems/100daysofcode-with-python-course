"""
Author: Ryan Monaghan
Date: 11/24/2018
Notes: Day 1 of 100 days of Code
"""

from datetime import datetime
from datetime import date
from datetime import timedelta

print(datetime.today())  # Year Month Day HR, MIN, SEC, MILLI

today = datetime.today()
print(type(today))  # <class 'datetiem.date'>

todaydate = date.today()
print(type(todaydate))  # <class 'datetime.date'>
print(todaydate)  # YEAR Month Day

print(todaydate.month)
print(todaydate.day)
print(todaydate.year)

christmas = date(2018, 12, 25)

print(christmas - todaydate)  # todaydate.timedelta(31)

(christmas - todaydate).days  # 31

if christmas is not todaydate:
    print("Sorry there are still", (christmas -
                                    todaydate).days, "days until christmas")
else:
    print("Yay it's christmas")


# Time Delta Notes - A gap in time


t = timedelta(days=4, hours=10)
print(type(t))

print(t.days)
print(t.seconds)  # goes up to 1 day, gives us the seconds in our hours

# t.hours doesn't work...

print(t.seconds / 60 / 60)  # seconds to hours


eta = timedelta(hours=6)
today = datetime.today()

print(today)
print(eta)

print(today + eta)  # can add timedeltas to datetime


# Play Time

rightnow = datetime.today()
future = timedelta(hours=6)

print("6 hours from now is", rightnow + future)
print("6 hours in the past is", rightnow - future)
