import random

def run_guess(guess,answer):
    if 0<guess<11:
        if guess==answer:
            print('You are a genuis')
            return True
        else:
            print('hey bozo i said 1~10')



if __name__=='__main__':
 answer=random.randint(1,10)

 while True:
     try:
        guess=int(input('guess a number 1~10'))
        if(run_guess(guess,answer)):
           break
     except ValueError:
        print('please enter a number')
        continue