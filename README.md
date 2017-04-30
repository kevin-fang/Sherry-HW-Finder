# Sherry Homework Finder

Given an input text file containing the homework for the current unit, run:  
`python findHW.py #` on Windows or simply `./findHW.py #` on OS X/Linux and the program will output the next homework that is due.   
The `#` value simply designates how far ahead wish to look for the homework. Leaving it blank will return the homework due tomorrow. Running `python findHW.py 1` will give you the homework due the day after tomorrow and running `python findHW.py -1` will give you the homework due today.

Note that you need to copy the contents of the current syllabus into `hw.txt`, otherwise the program will output "Incorrect Syllabus/No HW!"

---
### Features to be implemented in the future
* Automatic updating from drive? (next to impossible)
* Specify location of hw.txt?
