import sys

from introcs.stdlib import stdio

n = int(sys.argv[1])

factor = 2
while factor * factor <= n:
    while (n % factor) == 0:
        n //= factor
        stdio.write(f"{factor} ")
    factor += 1

if n > 1:
    stdio.write(n)
stdio.writeln()
