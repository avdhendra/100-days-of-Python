#dictionary
dictionary={
    'a':1,
    'b':2
}
print(dictionary['b'])
my_list=[
    {'a':[1,2,3],
    'b':'hello',
    'x':True
    }
]
print(my_list[0]['a'][2])

#dictionary key have special property a key has to be mutable
#because key is hash in function so if it change then we cannot the map the value
print(dictionary.get('b'))
print(dictionary.update({'b':20}))
print(dictionary)