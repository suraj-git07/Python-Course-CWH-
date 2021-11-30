#func to print the pattern
def patt(order):
   pattern="*"
   for i in order:      #no of rows
       for j in range(i):       #no of cols
           print(pattern,end="")
       print()
   
try:
   n=int(input("enter the boolean value 0 or 1"))  #pattern result as per 1 or 0
   order1=[1,2,3,4,5]
   order2=[5,4,3,2,1]

   if n==1:
      patt(order1)
   else:
      
      patt(order2)
except Exception as e:
    print(e)
