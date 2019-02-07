#! /etc/bin/env python3

'''
    Here we test iterators and generators
'''

def myrange(size):
    for i in range(size):
        yield i     

class iterator:
    def __next__():
        pass
    
def main():
    alist = myrange(10)
    print(list(alist))
        
        
if __name__ == '__main__': main()