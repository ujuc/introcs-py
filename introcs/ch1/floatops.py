import sys

from introcs.stdlib import stdio

a = float(sys.argv[1])
b = float(sys.argv[2])

total = a + b
diff = a - b
prod = a * b
quot = a / b
exp = a ** b

stdio.writeln(f"{a} + {b} = {total}")
stdio.writeln(f"{a} - {b} = {diff}")
stdio.writeln(f"{a} * {b} = {prod}")
stdio.writeln(f"{a} / {b} = {quot}")
stdio.writeln(f"{a} ** {b} = {exp}")
