import re, datetime

with open("hw.txt", "r") as f:
    buffer = f.read();
    today = datetime.date.today()
    details = re.search(r'(.*?)-(.*?)-(.*)', str(today))
    month = details.group(2)
    month = re.sub(r"0(.)", r"\1", month);
    day = details.group(3)
    day = int(re.sub(r"0(.)", r"\1", day));
    weekday = int(datetime.datetime.today().weekday())

    if weekday == 5:
        day += 2;
    elif weekday == 6:
        day += 1;

    regexSearch = re.compile(r"(.+%s\/%d.+)" % (month, day))
    
    todayHW = regexSearch.search(buffer);
    print todayHW.group(1)
