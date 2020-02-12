import random
import sys

from introcs.stdlib import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])

stdio.writeln(random.randint(a, b))
