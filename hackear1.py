
# Write your code here
n=int(input())
ar=input().split(" ")
res=map(lambda x:int(x),ar)
lis=list(res)
smallest=-1
options={}
sum=0
sm=[]
for i in range(0,n):   # finding ele that fullfil the condition
    for j in range(i+1,n):
        sum+=lis[j]
    if sum%7==0:
        options[i]=lis[i]    # this creates a dict on such elements 
# print(options)

for k in options.values(): # finding the smallest element from dict
    sm.append(k)
# print(sm)
sm.sort()
smval=sm[0] # smallest value from dict

#smallest value index
# function to return key for any value 
def get_key(val): 
    for key, value in options.items(): 
         if val == value: 
             return key 
smallest=get_key(smval) 
print(smallest)
