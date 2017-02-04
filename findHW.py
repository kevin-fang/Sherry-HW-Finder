import re, datetime
from sys import exit

with open("hw.txt", "r") as f:
    buffer = f.read();
    day = re.compile("\n(?=\w+)");
    dayWork = day.split(buffer)[1:]

    today = datetime.date.today()
    details = re.search(r'(.*?)-(.*?)-(.*)', str(today))
    month = details.group(2)
    month = int(re.sub(r"0(.)", r"\1", month));
    day = details.group(3)
    day = int(re.sub(r"0(.)", r"\1", day)) + 1;
    weekday = int(datetime.datetime.today().weekday())

for work in dayWork:
    i = 0
    while (i < 50):
        formedDay = re.compile("%s/%s" % (month, day + i))
        i += 1
        if formedDay.search(work):
            print work,
            exit(1)

print("Outdated Syllabus/No HW")
