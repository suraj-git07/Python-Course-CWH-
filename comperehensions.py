
# first list comprehensions
# foramt ls=[<what to add> <range loops> <conditions>]

# ls=[i for i in range(100) if i%3==0]
# print(ls)
#
# # second dict comprehensions
# # foramt ls={<what to add> <range loops> <conditions>}
# dict1={i:f"item{i}" for i in range(20) if i%5==0}
# print(dict1)
# # reversing dict using comprehensions
# dict2={value:key for key ,value in dict1.items()}
# print(dict2)
#
# # third set comprehensions
# ser1={i for i in range(10)}
# print(type(ser1))                      #in all classes diff can be spotted by parenthesis
# print(ser1)
#
# # forth generator comprehensions
# gen=(i for i in range(100) if i%2==0)
# print(type(ser1))
# print(gen)
# print(gen.__next__())


# _____________________________________________________________________________________________________

no_input=int(input("enter the no of times you want to enter the inputs"))
record = []
for i in range(no_input):
    inputs = input("enter the input")
    record.append(inputs)

typr_comp=input("enter the type of comprehensions")
if typr_comp=="listcomp":
    a =  [x for x in record]
    print(a)
elif typr_comp=="setcomp":
    a =  {x for x in record}
    print(a)
elif typr_comp=="gencomp":
    a =  (x for x in record)
    print(a)
    for i in range(no_input):
        print(next(a))

else:
    print("wronge input")