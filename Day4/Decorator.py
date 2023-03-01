#Decorator
def my_decorator(func):
    def wrap_func():
        print('******')
        func()
        print('******')
    return wrap_func

@my_decorator
def my_func():
    print('my_func')

my_func()

#decorator is to super boost the function
#or
def bye():
    print('see ya later')

hello2=my_decorator(bye)
hello2()




def decomeco(func):
    def wrap_func(x):
        print('******')
        func(x)
        print('******')
    return wrap_func

@decomeco
def my_func(x):
    print('my_func')

a=decomeco(my_func)
a('hii')