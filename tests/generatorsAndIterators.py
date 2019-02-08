#! /etc/bin/env python3

'''
    Here we test iterators and generators
'''

def generatorfunction(size):
    for i in range(size):
        yield i    
        
def modernFibonacci(order):
    """
    Modern fibonacci starts with 0, 1 fort the first two elements instead of 1, 1
    """
    last1 = 1
    last2 = 0
    for i in range(order):
        temp  = last1
        last1 = last1 + last2
        last2 = temp
        yield last1        

class iterator:
    def __next__():
        pass       
        
if __name__ == '__main__':     
    "First we test a generator function"
    agenerator = generatorfunction(5)
    print(agenerator)
    print(f'A generator function actually is an object: {type(agenerator)}')
    print(f'It\s also iterable: {int(agenerator.__next__())}')
    print(f'It\s also iterable: {int(agenerator.__next__())}')
    print(f'Feed it to a list to get the list:{list(agenerator.__iter__())}')
    
    "Test Fibonacci"
    order = 1
    print(f'Print fibonacci {order:>02}: {list(modernFibonacci(order))}')
    order = 3
    print(f'Print fibonacci {order:>02}: {list(modernFibonacci(order))}')
    order = 10
    print(f'Print fibonacci {order:>02}: {list(modernFibonacci(order))}')
    