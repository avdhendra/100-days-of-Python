print("Hello World")

# Fundamental Data Types
#int ,float,bool,str,list,tuple,set,dict
#complex for complex number in maths
#Classes -> Custom types

#Specialized Data Types

print(type(6))
print(2**3) #power 2^3
print(5//4) # gave quotient
print(6%4) #gave remainder

#math function
print(round(5/4))
print(abs(-20))

#print binary number
print(bin(5))
print(int('0b101',2)) #base as 2 convert binary to integer 

#string
username="supercoder"
password='supersecret'
long_string='''
WOW
0 0 
-----
'''
#string concatenation
print('hello'+ 'Andrei')

#Escape Sequence
weather=" IT\'s sunny" #after \ what come after \ is string
                                                               
#formatted String
name='Johnny'
age=55
print('hi'+name)
#format
print(f'hi {name} .you are {age} year old')
#or
print('hi {} ,you are {} years,old'.format(name,age))
#age 1 and name is 0 index

print('hi {1} ,you are {0} years,old'.format(name,age))
#age 1 and name is 0 index

#string indexes
selfish='01234567'
#[start:stop:stepover]
print(selfish[0:3:1])
#start at 1 and go to end
print(selfish[1:])
#start from 0 and go to 5-1
print(selfish[:5])
#reverse of string
print(selfish[::-1])


#string are immutable
###
stra='jins'
#stra[0]='10' #gave error 
#builtin function
greet='helloooo'
print(greet[0:len(greet)])

quote='to be or not to be'
print(quote.find('be'))

print(quote.replace("be",'2'))

#password Checker
username=input('what is your username')
password=input('what is your password')
password_len=len(password)
#this will hide the password in**** format
hidden_password='*'*password_len
print(f'{username},your password,{hidden_password},is {len(password)} letter long')






