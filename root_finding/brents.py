from scipy.optimize import brent
from math import sin
def f(x):
    return sin(x)
minimizer = brent(f, brack=(1, 4))
print(minimizer)
