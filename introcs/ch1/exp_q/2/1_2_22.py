import math
import sys

from introcs.stdlib import stdio

t = float(sys.argv[1])
v = float(sys.argv[2])

w = 34.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * math.pow(v, 0.16))

stdio.writeln(f"34.74 + (0.6215 * {t}) + ((0.4275 * {t}) - 35.75) * {v}^0.16 = {w}")
