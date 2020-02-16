import math
import sys

from introcs.stdlib import stdio

la0 = float(sys.argv[1])
pi = float(sys.argv[2])
lam = float(sys.argv[3])

x = lam - la0
y = (1 / (2 * math.log((1 + math.sin(pi)) / (1 - math.sin(pi)))))

stdio.writeln(f"x = {x}, y = {y}")
