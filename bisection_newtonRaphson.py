import matplotlib.pyplot as plt
import math
import numpy as np
import timeit

# the Newton-raphson method

def f(x):
    return x**4 - 4*x**3 - 11*x**2 + 40*x - 36

def df(x):
    return 4*x**3 - 12*x**2 - 22*x + 40

x0 = 1
tolerance = 1e-6
max_iterations = 100

i = 0
starttime = timeit.default_timer()

# Iterator used

for i in range(max_iterations):
    i += 1
    fx = f(x0)
    dfx = df(x0)
    x1 = x0 - fx/dfx
    if abs(f(x1)) < tolerance:
        print(f"Root at x = {x1:.6f}\n")
        break
    else:
        x0 = x1
print(f"NEWTON-RAPHSON:{timeit.default_timer()-starttime:.6f} milliseconds")



# Bbisection in action

a = 2
b = 3
tolerance = 1e-6
max_iterations = 100
starttime = timeit.default_timer()

for i in range(max_iterations):
    c = (a+b)/2
    
    if abs(f(c))<tolerance:
        print(f"Root at x = {c:.6f}")
        break;
    elif f(c)*f(a)<0:
        b =c
    else:
        a =c 
print(f"BISECTION:{timeit.default_timer() - starttime:.6f} milliseconds")