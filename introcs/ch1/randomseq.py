import random
import sys

from introcs.stdlib import stdio

n = int(sys.argv[1])
for i in range(n):
    stdio.writeln(random.random())
