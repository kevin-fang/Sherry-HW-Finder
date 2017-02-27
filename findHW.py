#!/usr/bin/env python

import re, datetime, sys

extraValue = 0

try:
    extraValue = int(sys.argv[1])
except:
    pass

with open("hw.txt", "r") as f:
    buffer = f.read()
     #lookahead to find each spacing between homework entries
    day = re.compile("\n(?=\w+)")
    #remove first entry as it contains headers to the data
    dayWork = day.split(buffer)[1:]

    #get current day, month, and weekday
    today = datetime.date.today()
    month = today.month
    day = today.day + 1 + extraValue
    weekday = int(today.weekday())

# search for homework in buffer
for work in dayWork:
    i = 0
    while (i < 50):
        formedDay = re.compile("%s/%s" % (month, day + i))
        i += 1
        if formedDay.search(work):
            print work,
            sys.exit(0)

print("Incorrect Syllabus/No HW")
