
def bsearch(li, item, last, beg):

        mid = int((beg+last)/2)
        if item==li[mid]:
            return mid
        elif item < li[mid]:
            last = mid- 1
            return bsearch(li, item, last, beg)
        else:
            beg=mid+1
            return bsearch(li, item, last, beg)

# _ _ main _ _

list1 = eval(input( "enter the list" ))
last = len(list1)-1
beg=0
item1 = int(input("enter the item"))
itemp = bsearch(list1, item1, last, beg)
print("THE REQUIRED ITEM IS IN PLACE: " ,itemp)
