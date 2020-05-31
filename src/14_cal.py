"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py [month] [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.

Note: the user should provide argument input (in the initial call to run the file) and not 
prompted input. Also, the brackets around year are to denote that the argument is
optional, as this is a common convention in documentation.

This would mean that from the command line you would call `python3 14_cal.py 4 2015` to 
print out a calendar for April in 2015, but if you omit either the year or both values, 
it should use today’s date to get the month and year.
"""

# no input (no argument) -> print calendar for current month
# one argument -> assume input is a month, render calendar for that month of this year
# two arguments -> assume month and year, render calendar for that month and year
# otherwise, print a usage statement to the terminal indicating the correct format

import sys
import calendar
from datetime import datetime

def renderCal(m=datetime.today().month, y=datetime.today().year):
    print(calendar.month(int(y), int(m)))

renderCal(*sys.argv[1:3])
if len(sys.argv) <= 1:
    print("Format should be: 14_cal.py [month] [year]")
    exit()

# from lecture explanation:
# access the arguments passed to the program
# print(sys.argv)
# num_args = len(sys.argv)
# month = None
# year = None

# if num_args == 1:
#   # no arguments
#   month = datetime.now().month
#   year = datetime.now().year
# elif num_args == 2:
#   # assuming the one argument is the desired month of this year
#   month = int(sys.argv[1])
#   year = datetime.now().year
# elif num_args == 3:
#   # user specified both month and year
#   month = int(sys.argv[1])
#   year = int(sys.argv[2])
# else:
#   # error message
#   print("usage: cal.py [month] [year]")
#   sys.exit(1)

# cal = calendar.TextCalendar()

# cal.prmonth(year, month)
  