import sys

from introcs.stdlib import stdio

n = int(sys.argv[1])

v = 1
while v <= n // 2:
    v *= 2

while v > 0:
    if n < v:
        stdio.write(0)
    else:
        stdio.write(1)
        n -= v
    v //= 2
