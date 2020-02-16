import sys

from introcs.stdlib import stdio

n = int(sys.argv[1])
power = 1
i = 0
while i <= n:
    stdio.writeln(f'{i} {power}')
    power = 2 * power
    i = i + 1
