#! /etc/bin/env/ python

'''
    Testing basic concepts of filter, map, reduce
    Course: http://book.pythontips.com/en/latest/map_filter.html
'''

newlist = list()

#How to define a lambda function
func = lambda x: x**2
print(func(4))

#How to iter on a lambda function using map()
x = range(10)
result = list(map(lambda x: x**2, x))
print(result)

'''
    map() can also use functions as inputs, lambda can be used within a loop
'''
def multiply(x):
    return x*x
def add(x):
    return (x+x)

funcs = [multiply, add] # thats a list of functions

for i in range(5):
    value = list(map(lambda x:x(i), funcs))
    print(value)

'''
    filter() does return list elements, that evaluate to true, in a inner function
    this returns the list elements which are multiples of 2
'''
input = [1 ,2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(filter(lambda x: x%2 == 0, input)))


'''
    reduce()  does a rolling calculation on each element of a list
'''

from functools import reduce
alist = [1,2,3,4]
product = reduce(lambda x,y: x * y, alist)
print(f'Product of list: {product}')



