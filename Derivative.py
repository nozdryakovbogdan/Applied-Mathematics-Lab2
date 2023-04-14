from sympy import diff, symbols, sin

x = symbols('x')

print("y' = (sin(2*x + 4) + 4)' - ", diff(sin(2*x + 4) + 4))

print("")

print("y' = (x**2 + 14)' - ", diff(x**2 + 14))