from datetime import datetime
from datetime import date
from datetime import timedelta

start = datetime(2015, 10, 3, 10, 12, 51)
end = datetime(2015, 9, 3, 2, 11, 22)

print(start)
print(end)
print((end-start))


start_100days = date(2017, 3, 30)
pybites_founded = date(2016, 12, 19)
pycon_date = date(2018, 5, 8)


def get_hundred_days_end_date():
    """Return a string of yyyy-mm-dd"""
    return str(start_100days+timedelta(days=100))


def get_days_between_pb_start_first_joint_pycon():
    """Return the int number of days"""
    return (pycon_date-pybites_founded).days

print(str(get_hundred_days_end_date()) == '2017-07-08')
print(get_days_between_pb_start_first_joint_pycon())


THIS_YEAR = 2018
date = '1 Oct, 2010'

def years_ago(date):
    """Receives a date string of 'DD MMM, YYYY', for example: 8 Aug, 2015
       Convert this date str to a datetime object (use strptime).
       Then extract the year from the obtained datetime object and subtract
       it from the THIS_YEAR constant above, returning the int difference.
       So in this example you would get: 2018 - 2015 = 3"""
    #pass
    theDate = datetime.strptime(date, "%d %b, %Y").year
    return THIS_YEAR - theDate
    
years_ago(date)


def convert_eu_to_us_date(date):
    """Receives a date string in European format of dd/mm/yyyy, e.g. 11/03/2002
       Convert it to an American date: mm/dd/yyyy (in this case 03/11/2002).
       To enforce the use of datetime's strptime / strftime (over slicing)
       the tests check if a ValueError is raised for invalid day/month/year
       ranges (no need to code this, datetime does this out of the box)"""
    #pass
    theDate = datetime.strptime(date,"%d/%m/%Y")
    return theDate.strftime("%m/%d/%Y")

convert_eu_to_us_date("11/03/2002")