import sys
import math

from introcs.stdlib import stdio

n = int(sys.argv[1])

if n < 0:
    exit(1)

for number in range(1, n+1):
    if math.log2(number) % 1 == 0:
        stdio.writeln(f"{number}")
