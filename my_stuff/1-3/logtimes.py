'''Extract datetimes from log entries and calculate the time
   between the first and last shutdown events'''
from datetime import datetime
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
logfile = os.path.join('/tmp', 'log')
urllib.request.urlretrieve('http://bit.ly/2AKSIbf', logfile)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    '''TODO 1:
       Given a log line extract its timestamp and convert it to a datetime object. 
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
           01234567890123456789
       returns:
       datetime(2014, 7, 3, 23, 27, 51)'''
    index_of_space = int(line.find(" "))
    year = int(line[index_of_space+1 : index_of_space+5])
    month = int(line[index_of_space+6 : index_of_space+8])
    day = int(line[index_of_space+9 : index_of_space+11])
    hour = int(line[index_of_space+12 : index_of_space+14])
    minute = int(line[index_of_space+15 : index_of_space+17])
    second = int(line[index_of_space+18 : index_of_space+20])
    return datetime(year, month, day, hour, minute, second)


def time_between_shutdowns(loglines):
    '''TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and calculate the 
       timedelta between the first and last one. 
       Return this datetime.timedelta object.'''
    #start, end = datetime.today()
    for line in loglines:
        if "Shutdown initiated." in line:
            start = convert_to_datetime(line)
            break
    end = convert_to_datetime(loglines[-1])        
    return end-start