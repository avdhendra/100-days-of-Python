#parameters
def say_hello(name,emoji):
    print(f'hellon {name} got {emoji}')

#positional argument
say_hello("andrei","smile")

#default parameter
def good_bye(name='Fc',emohi='lol'):
    print(f'{name},{emohi}')

good_bye()


#walrus operator :=
a='heloo'
if((n:=len(a))<10):
    print(f'to small{n}')

total=0

def count():
    #to access the global variable
    global total
    total+=1
    return total

count()
