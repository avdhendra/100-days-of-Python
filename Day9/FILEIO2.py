#another way to read file without cursor problem
#mode is file operation
#read=r
#write=w
#read and write=rw
#append =a
with open('test.txt',mode='r') as my_file:
    print(my_file.readlines())
with open('test.txt',mode='w') as my_file:
    text=my_file.write('hello guys')