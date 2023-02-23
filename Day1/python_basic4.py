my_tuple=(1,2,3,4,5)
#tuple is immutable
print(5 in my_tuple)
#why tuple if we have list ?->> if we dont want any change in tuple
#tuple is valid key in dictionary
#print(user[(1,2)])
x,y,z, *other=(1,2,4,5,6)
print(other)

#method of tuple
print(my_tuple.count(5))
print(my_tuple.index(5))
