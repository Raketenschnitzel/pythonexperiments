from scipy.optimize import fsolve
import numpy as np
import math
import matplotlib.pyplot as plt

def func(x):
    return x + 2*math.cos(x)

def func1(x):
    out = [x[0]*math.cos(x[1]) - 4]
    out.append(x[1]*x[0] - x[1] - 5)
    return out

def func3(x):
    out = [x[0]**2 + x[1] + 1]
    out.append(-1*x[0]**2 -1* x[1] + 10)
    return out

def func4(x, y):
    return np.sin(y * x)

x0 = fsolve(func, 0.3)
print(x0)

x01 = fsolve(func1, [1, 1])
print(x01)

x02 = fsolve(func3, [1, 1])
print(x02)

##crazy stuff i dont understand yet
#xaxis = np.linspace(0, 4, 10)
#yaxis = np.linspace(-1, 1, 20)
#result = func4(xaxis[:,None], yaxis[None,:])
#print(result)


#plot func3
x = np.linspace(0,10,10)
result = func3(x)
print('Input')
print(x)
print('This is the result of equation system:')
print(result)
