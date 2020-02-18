import sys

from introcs.stdlib import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a == b == c:
    stdio.writeln('equal')
else:
    stdio.writeln('not equal')
