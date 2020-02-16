import sys

from introcs.stdlib import stdio

r = int(sys.argv[1])
g = int(sys.argv[2])
b = int(sys.argv[3])

w = max(r / 255, g / 255, b / 255)
c = (w - (r / 255)) / w
m = (w - (g / 255)) / w
y = (w - (b / 255)) / w
k = 1 - w

stdio.writeln(f"c: {c}, m: {m}, y:{y}, k: {k}")
