#! /etc/bin/env python3

'''
    Here we test iterators and generators
'''

def generatorfunction(size):
    for i in range(size):
        yield i    
        
def modernFibonacci1(order):
    """
    Modern fibonacci starts with 0, 1 fort the first two elements instead of 1, 1
    generator implementation
    """
    last1 = 1
    last2 = 0
    for i in range(order):
        temp  = last1
        last1 = last1 + last2
        last2 = temp
        yield last1 
        
def modernFibonacci2(order):
    """
    More pythonic version of modernFibonacci1.
    This way we omit the temp variable
    """
    last1, last2 = 1, 0
    for i in range(order):
        last1, last2 = last1 + last2, last1
        yield last1          
        
def fibonacci2(n):
    """
    list implementation
    more ressources needed
    """
    a = b = 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result    

class iterator:
    def __next__():
        pass       
        
if __name__ == '__main__':     
    "First we test a generator function"
    agenerator = generatorfunction(5)
    print(agenerator)
    print(f'A generator function actually is an object: {type(agenerator)}')
    print(f'It\s also iterable: {int(next(agenerator))}')
    print(f'It\s also iterable: {int(next(agenerator))}')
    print(f'Feed it to a list to get the list:{list(agenerator.__iter__())}')
    
    "Test Fibonacci"
    order = 1
    print(f'Print modernFibonacci1 {order:>02}: {list(modernFibonacci1(order))}')
    order = 3
    print(f'Print modernFibonacci1 {order:>02}: {list(modernFibonacci1(order))}')
    order = 10
    print(f'Print modernFibonacci1 {order:>02}: {list(modernFibonacci1(order))}')
    
    order = 1
    print(f'Print modernFibonacci2 {order:>02}: {list(modernFibonacci2(order))}')
    order = 3
    print(f'Print modernFibonacci2 {order:>02}: {list(modernFibonacci2(order))}')
    order = 10
    print(f'Print modernFibonacci2 {order:>02}: {list(modernFibonacci2(order))}')
    
    "Test runtime"
    order = 100000
    print(f'Print modernFibonacci2 {order:>02}: {sum(modernFibonacci2(order))}')   