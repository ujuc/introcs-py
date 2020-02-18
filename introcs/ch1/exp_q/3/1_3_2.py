import sys

from introcs.stdlib import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

if a == 0:
    a = 1

d = b * b - 4 * a * c

if d < 0:
    stdio.writeln('positive')
else:
    stdio.writeln(d)
