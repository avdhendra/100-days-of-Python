my_file=open('test.txt')

print(my_file.read())
my_file.seek(0) #set the cursor to initial position
print(my_file.read())
my_file.seek(0)
print(my_file.readline())
print(my_file.readline())
my_file.seek(0)
print(my_file.readlines()) #read alll lines 

my_file.close()