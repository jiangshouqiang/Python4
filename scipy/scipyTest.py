#-*- coding: utf-8 -*
from scipy.optimize import fsolve

def f(x):
    x1 = x[0]
    x2 = x[1]
    return [2*x1 - x2*2 - 1 ,x1**2 - x2 - 2]

result = fsolve(f,[1,1])
print(result)

from scipy import integrate
def g(x):
    return (1-x**2)**0.5
pi_2,err = integrate.quad(g,-1,1)
print(pi_2 * 2)