import random

from introcs.stdlib import stdio

o = random.random()
t = random.random()
th = random.random()
fo = random.random()
fi = random.random()

arg = (o + t + th + fo + fi) / 5

stdio.writeln(
    f"arg = {arg}, min = {min(o, t, th, fo, fi)}, max = {max(o, t, th, fo, fi)}"
)
