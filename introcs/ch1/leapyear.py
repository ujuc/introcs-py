import sys

from introcs.stdlib import stdio

year = int(sys.argv[1])

isLeapYear = (year % 4 == 0)
isLeapYear = isLeapYear and ((year % 100) != 0)
isLeapYear = isLeapYear or ((year % 400) == 0)

stdio.writeln(isLeapYear)
