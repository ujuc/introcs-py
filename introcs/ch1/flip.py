import random

from introcs.stdlib import stdio

if random.randrange(0, 2) == 0:
    stdio.writeln('앞')
else:
    stdio.writeln('뒷')
