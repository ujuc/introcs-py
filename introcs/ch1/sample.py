import random
import sys

from introcs.stdlib import stdarray, stdio

m = int(sys.argv[1])
n = int(sys.argv[2])

perm = stdarray.create_1d(n, 0)
for i in range(n):
    perm[i] = i

for i in range(m):
    r = random.randrange(i, n)

    temp = perm[r]
    perm[r] = perm[i]
    perm[i] = temp

for i in range(m):
    stdio.write(f"{perm[i]} ")
stdio.writeln()
