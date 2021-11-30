"""
iterable=objects which have methods defined on them,__iter__()  or __getitem__()

iterator=objects which have __next()  using this we iterate the iterable

iteration=process of iterating

"""
# generator - it is basically a func which yield a value(generate one value at that time) but only return when we want . also it returns values one by one whereas a normal func returns all the value in a single go
# formaing a self generator

def gen(n):
    for i in range(n):
        yield  i      #it is agenerator it generate a value on a fly
        # use because we dont want that a huge no is first save on our memry thst print
        # here it generate that print than further generate

n=gen(5)  #genetating generator object
print(n)   #give object name
print(n.__next__()) #i told u above
print(next(n))    #another way to apply next func on generator obeject
print(n.__next__())
print(n.__next__())
print(n.__next__())
# # after this it will give me error
# print(n.__next__()) # since abvome my iteration stops

# for range() has a inbuilt stopper