from introcs.stdlib import stdio

for i in range(1000, 2000):
    stdio.write(f"{i} ")
    if (i % 5) == 0:
        stdio.writeln()
