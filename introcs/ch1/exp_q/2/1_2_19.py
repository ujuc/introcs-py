import sys

from introcs.stdlib import stdio

x0 = float(sys.argv[1])
v0 = float(sys.argv[2])
t = float(sys.argv[3])
G = 9.80665

stdio.writeln(f"x0 + v0t - Gt^2 / 2 = {x0 + (v0 * t) - ((G * (t ** 2)) / 2)}")
