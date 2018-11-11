from scipy.optimize import *
from numpy import *

#course video
#https://www.youtube.com/watch?reload=9&v=S4Qg2CsiIj8

def equationSystem1(z):
    x = z[0]
    y = z[1]
    #w = z[2]

    F       = empty(2)
    F[0]    = pow(x,2) + pow(y,2) - 20
    F[1]    = pow(x,2) - y
    #F[2]    = x * y - w - 5

    return F

result = fsolve(equationSystem1, [1,1])
print('Result:')
print(result)

# testing to split functions

def circle(z):
    x       = z[0]
    y       = z[1]
    F       = pow(x,2) + pow(y,2) - 20
    return F

def parabel(z):
    x       = z[0]
    y       = z[1]
    F       = pow(x,2) - y
    return F

def equationSystem2(z):

    F       = empty(2)
    F[0]    = circle(z)
    F[1]    = parabel(z)

    return F

result = fsolve(equationSystem2, [1,1])
print('Result:')
print(result)
