import math
import sys

from introcs.stdlib import stdio

x1 = float(sys.argv[1])
y1 = float(sys.argv[2])
x2 = float(sys.argv[3])
y2 = float(sys.argv[4])

x1 = math.radians(x1)
y1 = math.radians(y1)
x2 = math.radians(x2)
y2 = math.radians(y2)

angle1 = math.acos(
    math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)
)

angle1 = math.degrees(angle1)

delta = 60 * angle1

stdio.writeln(f"delta: {delta}")
