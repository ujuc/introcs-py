import sys

from introcs.stdlib import stdio

n = int(sys.argv[1])

total = 0.0
for i in range(1, n + 1):
    total += 1.0 / i
stdio.writeln(total)
