#!/bin/bash/env python

import re, datetime, sys

extraValue = 0

try:
    extraValue = int(sys.argv[1])
except:
    pass

with open("hw.txt", "r") as f:
    buffer = f.read()
    day = re.compile("\n(?=\w+)")
    dayWork = day.split(buffer)[1:]

    today = datetime.date.today()
    month = today.month
    day = today.day + 1 + extraValue
    weekday = int(datetime.datetime.today().weekday())

for work in dayWork:
    i = 0
    while (i < 50):
        formedDay = re.compile("%s/%s" % (month, day + i))
        i += 1
        if formedDay.search(work):
            print work,
            sys.exit(0)

print("Incorrect Syllabus/No HW")
