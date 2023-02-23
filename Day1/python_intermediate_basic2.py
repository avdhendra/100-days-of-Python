#print each item in string
for item in 'Zero to Mastery':
    print(item)
for item in (1,2,3,4):
    print(item)
for item in {1,2,4,3}:
    print(item)

    #for dictionary
    user={
        'name':"God",
        'age':501,
        'can_swim':False
    }
    for item in user.items():
        print(item)
    for item in user.values():
        print(item)
    for item in user.keys():
        print(item)

    for k,v in user.items():
        print(k,v)

#range
for _ in range(0,10): # _ if you dont want to have a variable

    print("hello")

for _ in range(10,0,-1):
    print(_)
i=0
while i<10:
    print(i)
    i+=1

picture=[[0,0,0,1,0,0,0],[0,0,1,1,1,0,0],[0,1,1,1,1,1,0],[1,1,1,1,1,1,1],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0]]

#iterate over picture
# if 0 -> print ' '
#if 1 -> print *

siz=len(picture)
for item in picture:
    for pixel in item:
        if pixel==0:
          print(" ",end='')
        elif pixel==1:
           print("*",end="")
    
    print("\n")