#! /etc/bin/env python3

import random

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

class MyCounter:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        self.temp = self.a
        self.a +=1
        return self.temp     

class RandomIterable:
    """
    Just a demonstrator for Iterables
    It's kind of rolling a six sided die with 5 x 1 and 1 x StopIteration
    """
    def __iter__(self):
        self.options = ('go', 'go', 'go', 'go', 'go', 'stop')
        return self

    def __next__(self):
        if random.choice(self.options) == 'go':
            return 1
        else:
            raise StopIteration                   
        
if __name__ == '__main__':     
    """
    Generators are Iterators. You can only iterate over them once. 
    They can be implemented as function using keyword yield. 
    Iterators are classes which implement __next__() function
    You can call next() on them.
    Iterables implement __iter__() function.
    You can call iter() on them. This creates an Iterator.
    An Iterable can implement __next__() itself.
    """
    agenerator = generatorfunction(5)
    print(agenerator)
    print(f'A generator function actually is an object: {type(agenerator)}')
    print(f'It\'s also iterable: {int(next(agenerator))}')
    print(f'It\'s also iterable: {int(next(agenerator))}')
    print(f'Feed it to a list to get the list:{list(agenerator)}')
    try:
        print(f'It\s also iterable: {int(next(agenerator))}')
    except StopIteration: 
        print("""
              End of iterator reached. Exception is thrown!
              """.upper())
    
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
    #order = 100000
    #print(f'Print modernFibonacci2 {order:>02}: {sum(modernFibonacci2(order))}')  
    
    """
    Test MyCounter
    MyCounter is an Iterable!
    You can create the Iterator by invoking iter()
    The iterator is implements the next() function. 
    """
    
    aCounter    = MyCounter()
    aIterator   = iter(aCounter)
    print(next(aIterator))
    print(next(aIterator))
    print(next(aIterator))
    print(next(aIterator))
    
    """
    Test RandomIterable()
    Iterables can be passed to for loops
    """
    print('Let\'s test the RandomIterable() object in a for loop:')
    for eggs in RandomIterable():
        print(eggs, end=', ')
    print('The for loop is catching the StopIteration exception :)')
    