#lambda Expression
my_list=[1,2,3]

#lambda function declare in a line

print(list(map(lambda item:item*2,my_list)))


#Square of numbers
my_list=[5,4,3]
new_list=list(map(lambda num:num**2,my_list))
print(new_list)

#list Sorting
a=[(0,2),(4,3),(10,-1),(9,9)]
#sort based on index 1 element in list of tuple
a.sort(key=lambda x:x[1])
print(a)



#list compreshion

my_list=[char for char in 'hello']
print(my_list)
my_list2=[num**2 for num in range(0,100)]
print(my_list2)

my_list3=[num**2 for num in range(0,100) if num%2==0]



#dictionary
simple_dict={
    'a':1,
    'b':2
}
my_dict={key:value**2 for key,value in simple_dict.item()}