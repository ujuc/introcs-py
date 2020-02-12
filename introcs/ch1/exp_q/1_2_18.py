import math
import sys

from introcs.stdlib import stdio

t = float(sys.argv[1])

stdio.writeln(f"sin(2t) + sin(3t) = {math.sin(2 * t) + math.sin(3 * t)}")
