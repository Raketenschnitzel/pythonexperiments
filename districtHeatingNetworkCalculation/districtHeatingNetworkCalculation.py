from scipy.optimize import *
from numpy import *
import math
import matplotlib.pyplot as plt

# general functions
def pressurePump(m, a):
    a2 = a[0]
    a1 = a[1]
    a0 = a[2]

    dp = a2 * m**2 + a1 * m + a0
    return dp

def pressureLoss(m, b):
    dp = b * m**2
    return dp

#calculation System 2

def equationSystem2(z):
    m0      = z[0]
    m1      = z[1]
    m2      = z[2]

    Pu1     = empty(3)
    Pu1[0]  = -1
    Pu1[1]  = 0.5
    Pu1[2]  = 12
    Loss1   = 0.05
    Loss2   = 0.08

    F       = empty(3)
    F[0]    = pressurePump(m0, Pu1) + pressureLoss(m1, Loss1)
    F[1]    = pressureLoss(m2, Loss2) - pressureLoss(m1, Loss1)
    F[2]    = m0 - m1 - m2

    return F

print('Massflows for System2')
result = fsolve(equationSystem2, [1, 0.5, 0.5])
print(result)


#calculation System 3
def equationSystem3(z):
    m0      = z[0]
    m1      = z[1]
    m2      = z[2]
    m3      = z[3]
    m4      = z[4]

    Pu1     = empty(3)
    Pu1[0]  = -1
    Pu1[1]  = 0.5
    Pu1[2]  = 12
    Pu2     = empty(3)
    Pu2[0]  = -1
    Pu2[1]  = 0.5
    Pu2[2]  = 12
    Loss1   = 0.05
    Loss2   = 0.08

    F       = empty(5)
    F[0]    = pressurePump(m0, Pu1) + pressureLoss(m1, Loss1)
    F[1]    = pressureLoss(m3, Loss2) - pressureLoss(m1, Loss1)
    F[2]    = pressureLoss(m3, Loss2) + pressurePump(m4, Pu2)
    F[3]    = m0 - m1 - m2
    F[4]    = m2 + m4 - m3

    return F

print('Massflows for System3')
result = fsolve(equationSystem3, [1, 0.25, 0.75, 0.25, 1])
print(result)
