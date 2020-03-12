import random
import sys

from introcs.stdlib import stdarray, stdio

n = int(sys.argv[1])

count = 0
collectedCount = 0
isCollected = stdarray.create_1d(n, False)

while collectedCount < n:
    value = random.randrange(0, n)
    count += 1
    if not isCollected[value]:
        collectedCount += 1
        isCollected[value] = True

stdio.writeln(count)
