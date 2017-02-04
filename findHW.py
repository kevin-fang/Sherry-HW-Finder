import re, datetime
from sys import exit

with open("hw.txt", "r") as f:
    buffer = f.read();
    today = datetime.date.today()
    details = re.search(r'(.*?)-(.*?)-(.*)', str(today))
    month = details.group(2)
    month = int(re.sub(r"0(.)", r"\1", month));
    day = details.group(3)
    day = int(re.sub(r"0(.)", r"\1", day)) + 1;
    weekday = int(datetime.datetime.today().weekday())

    i = 0;

    while (i < 50):
        regexSearch = re.compile(r"(.+. %d\/%d(?:.+)\n(?:\s+(?:p.+))?)" % (month, day + i))
        i += 1
        todayHW = regexSearch.search(buffer);
        try:
            print todayHW.group(1)
            exit(0)
        except AttributeError:
            pass
print("Outdated Syllabus/No HW!")
