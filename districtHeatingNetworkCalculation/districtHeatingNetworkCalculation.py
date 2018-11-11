from scipy.optimize import *
from numpy import *
import math
import matplotlib.pyplot as plt

#calculation System 2

def pressurePump1(m):
    a2 = -1
    a1 = 0.5
    a0 = 12

    dp = a2 * m**2 + a1 * m + a0
    return dp

def pressureLoss1(m):
    b1 = 0.05

    dp = b1 * m**2
    return dp

def pressureLoss2(m):
    b2 = 0.08

    dp = b2 * m**2
    return dp

def equationSystem2(z):
    m0      = z[0]
    m1      = z[1]
    m2      = z[2]

    F       = empty(3)
    F[0]     = pressurePump1(m0) + pressureLoss1(m1)
    F[1]     = pressureLoss2(m2) - pressureLoss1(m1)
    F[2]     = m0 - m1 - m2

    return F

print('Massflows for System1')
result = fsolve(equationSystem2, [1, 0.5, 0.5])
print(result)
