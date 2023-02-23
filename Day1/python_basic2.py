li=[1,2,3,5,4] # list is basically array in different langauge
li2=['a','b','c'] #character array
li3=[1,2,'a',True] #we can add different element in array

#Datastructure

amazon_cart=['box','pencil']
#index accessing element
print(amazon_cart[0])


#list slicing
amazon_cart=['notboo','sunglasses','toyes']
print(amazon_cart[0::2])

#list is mutable
amazon_cart[1]='jockey'
print(amazon_cart)

#matrix #multidimensional List

matrix=[[1,2],[2,3],[4,6]]
print(matrix[0][1])


#List methods apply to list
basket=[1,2,3,4,5]
#adding
print(basket.append(100)) ##end of the list # changes is apply to same variable inplace change
#insert the element at particular index
print(basket.insert(4,33))

#extend 
print(basket.extend([1001,1002]))
#removing
#pop return value that remove
basket.pop() # end of the list is removed
print(basket)
basket.pop(0) # remove item in index

basket.remove(4)
print(basket)
#clear remove everything in the list
print(basket.clear())

hisket=['a','b','c','d']
#print index of element
print(hisket.index('d'))
#optional where to start looking
print(hisket.index('d',0,4)) 
print('d' in hisket) #get true

#count the number of freq of element
print(basket.count('a'))

jisket=[1,2,3,46,5]
jisket.sort() #inplace sort
print(jisket)

print(sorted(jisket)) #create a new copy
jisket.reverse() #not sort the element
# it just reverse the element
#range
print(list(range(1,20))) #last element not count

#list unpacking
a,b,c=[1,2,3]
print(a,b,c)

a,b,c,*other,d=[1,2,3,4,55,47]
print(a,b,c,other,d)
