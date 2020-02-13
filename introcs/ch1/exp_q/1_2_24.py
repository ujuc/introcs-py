import math
import random

from introcs.stdlib import stdio

u = random.random()
v = random.random()

w = math.sin(2 * math.pi * v) * math.pow((-2 * math.log(u)), 1 // 2)

stdio.writeln(f"w = {w}")
