#every thing that is generators are iterable but --> range
#every iterable in not generator like list 


def generator_function(num):
    for i in range(num):
        yield i*2 # pause the function until the next
# held one item in memory
# for item in generator_function(100):
#     print(item)


g=generator_function(100)
print(g)
print(next(g))
print(next(g))




# def make_list(num):
#     result=[]
#     for i in range(num):
#         result.append(i*2)
#     return result

# my_list=make_list(100)
