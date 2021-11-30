def bubblesort(li):
    n=len(li)
    for i in range(0,n):
       for j in range(0,n-i-1):

         if li[j]>li[j+1]:
            li[j],li[j+1]=li[j+1], li[j]
         else:
            pass
    return li
#for testing
li=[1,2,3,7,6,5,4]
print("original list:",li)
l1=bubblesort(li)
print("list after sorting:",l1)



# def insertionsort(li):