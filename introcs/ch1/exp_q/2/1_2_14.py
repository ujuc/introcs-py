from introcs.stdlib import stdio

G = 9.8
mass1 = 10
mass2 = 20
radius = 20

force = G * mass1 * mass2 / radius * radius
stdio.writeln(force)

force2 = (G * mass1 * mass2) / (radius ** 2)
stdio.writeln(force2)
