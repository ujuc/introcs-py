import math
import sys

from introcs.stdlib import stdio

t = int(sys.argv[1])
P = float(sys.argv[2])
r = float(sys.argv[3])

stdio.writeln(f"{P * math.exp(r * t)}")
