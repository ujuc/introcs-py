import math
import sys

from introcs.stdlib import stdio

theta = float(sys.argv[1])

cos = math.cos(theta)
sin = math.sin(theta)

cos_sqrt = cos ** 2
sin_sqrt = sin ** 2

stdio.writeln(f"{cos_sqrt}, {sin_sqrt}")
stdio.writeln(f"{cos_sqrt + sin_sqrt}")
