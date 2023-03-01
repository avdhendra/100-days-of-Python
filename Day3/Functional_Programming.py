#pure function
#rules to be pure function
#rule1:
#give the same input 
#and return the the same output in each run of the program
#rule2
#does it have any side effect mean it take something from outside the function
#it doesnt effect out side world

#function map,filter,zip,and reduce
my_list=[1,2,3]
def multiple_by2(item):
    return item*2    

print(list(map(multiple_by2,[1,2,3])))

print(list(map(multiple_by2,my_list)))

#filter
def only_odd(item):
    return item%2!=0

print(list(filter(only_odd,my_list)))
print(my_list)


#zip all the iteratable element can be zip tupe array dictonary set
my_list=[1,2,3]
your_list=[10,20,30]
print(list(zip(my_list,your_list))) # we can zip as many iterable as we can

from functools import reduce

#reduc
def accumulator(acc,item):
    print(acc,item)
    return acc+item

print(reduce(accumulator,my_list,10))

print(my_list)