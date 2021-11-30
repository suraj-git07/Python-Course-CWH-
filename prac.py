# def revstr(st,n):
#     '''here str is sting and n=index value of last element'''
#
#     if n==0 :
#         return (str[0])
#     elif n>0:
#
#         return str[n] + revstr(st,n-1)
#
# # print(help(revstr))
#
# # __main__
# str=input("enter the string")
# n=len(str)-1
# print(revstr(str,n))
#
#
#
# # gcd
# def gcd(p,q):
#     if q==0:
#         return p
#     else:
#         return gcd(q,p%q)
#
# print(gcd(2,4))



# fibonacci
# def fib(n):
#     if n==1:
#         return 0
#     elif n==2:
#         return 1
#     else:
#         return fib(n-1)+fib(n-2)

# print(fib(4))


# binary search
# def bins(arry,beg,last,ele):
#     mid=int((beg+last)/2)
#     if arry[mid]==ele:
#         return mid
#     elif arry[mid]>ele:
#         last=mid-1
#         return bins(arry,beg,last,ele)
#     else:
#         beg=mid+1
#         return bins(arry,beg,last,ele)
#
# arry=eval(input("enter the list"))
# ele=int(input("enter the elemnet you want to search"))
# last=len(arry)-1
# beg=0
# print(bins(arry,beg,last,ele))
# import  bisect
# list1=[1,2,3]
# list1.insert(3,5)
# print(list1)
# print(bisect.bisect(list1,4))

# def posf(ar,ele):
#
#     if ele<ar[0]:
#       pos=0
#       return pos
#     else:
#       pos = -1
#       return pos
#
#     for i in range(len(ar)-1):
#         if ar[i]<ele and ele<ar[i+1]:
#             pos=i+1
#             return pos
#
#     if pos==-1:
#         return pos
#         #
# ar=[1,2,5]
# ele=6
# print(posf(ar,ele))
