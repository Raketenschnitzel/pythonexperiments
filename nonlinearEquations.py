from scipy.optimize import *
from numpy import *

#course video
#https://www.youtube.com/watch?reload=9&v=S4Qg2CsiIj8

def equationSystem(z):
    x = z[0]
    y = z[1]
    #w = z[2]

    F       = empty(3)
    F[0]    = pow(x,2) + pow(y,2) - 20
    F[1]    = pow(x,2) - y
    #F[2]    = x * y - w - 5

    return F

result = fsolve(equationSystem, [1,1,1])
print('Result:')
print(result)

#plot solution
