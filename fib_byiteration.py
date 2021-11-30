n=int(input("enter the number of terms you want to get"))
temp=0
first=0
sec=1

print(first,end=" ")
print(sec , end=" ")
for i in range (n-2):
   
    temp=first+sec
    print(temp, end=" ")
    first=sec
    sec=temp
    

    
