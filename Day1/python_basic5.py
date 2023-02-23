#set
my_set={1,2,3,4,5}
#unordered collection of unique object
my_set2={1,22,22,4}
print(my_set,my_set2)
list_my=[1,2,2,3]
print(set(list_my))
#set object not support indexing
print(list_my[1])


#method in set
my_set={1,2,3,4,5,6,7,8}
your_set={1,2,4,5,7}

#difference
print(my_set.difference(your_set))
#discard
my_set.discard(5)
print(my_set)
#difference update remove the non simlar things from set
print(my_set.difference_update(your_set))
print(my_set)

print(my_set.intersection(your_set))
#is any thing  common in set
print(my_set.isdisjoint(your_set))

print(my_set.union(your_set))

#issubset() and .issuperset()