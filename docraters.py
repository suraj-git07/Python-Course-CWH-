# # we can assign any func to a variable same as we give it a value
# a=print
# a("hello")


# we can also retuen a func using a func

# def func(a):
#     if a==0:
#         return print
#     elif a==1:
#         return sum
#
# b=func(1)
# print(b)

# now concept of decorators, decorators are use to assign a func to another function ,(see the ex)
# format of making a func dec of another-@<initial func name>
# decorator is any collable function tat can modiy the existing function
# ----------------------------------------------------------------------------------------------------
# def func2(func):
#     def upper():
#         str=func()
#         str=str.upper()
#         return str
#     return upper()
#
# @func2
# def func1():
#     return  "hi my name is func1"
#
# print(func1)
# -------------------------------------------------ex-2--------------------------------

# def division(a,b):
#     return a/b

# print(division(4,2))   #here showing no prob but
# print(division(1,0))   #as expec. it will shows an error , but if we don't want to change the exixting func we can make a deco

# making deco func which do the work of checking any zero divisor
def check(func):
    def change_if(a,b):
        if b==0:
            return "please give a logical input"     #if return
        return  func(a,b)    #else return
    return change_if

@check
def division(a,b):
    return a/b
print(division(1,0))