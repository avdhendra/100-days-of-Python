#Decorator for Performance Checking
from time import time
def performance(fn):
    def wrapper(*args,**kawrgs):
        t1 = time()
        result = fn(*args,**kawrgs)
        t2 = time()
        print(f'Function {fn.__name__} took {t2-t1} seconds')
        return result
    return wrapper

@performance
def long_time():
    print('1')
    for i in range(1000): #range in generator
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(100)): #range is iterable
        i*5


long_time()
long_time2()