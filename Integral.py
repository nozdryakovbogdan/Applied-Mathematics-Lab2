from scipy import integrate

def f(x):

    return x**3 + 3 * x

v, err = integrate.quad(f, -10, 20)

print(v)