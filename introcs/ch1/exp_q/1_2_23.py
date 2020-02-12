import math
import sys

from introcs.stdlib import stdio

x = float(sys.argv[1])
y = float(sys.argv[2])

r = math.sqrt((x ** 2) + (y ** 2))
theta = math.atan2(y, x)

stdio.writeln(f"r = {r}, theta = {theta}")
