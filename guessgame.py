import random
a=random.randint(0,100)

k=0
while k<=6:
  j=int(input("enter the guees number"))
  if j==a:
    print("you won buddy")
    break
  elif j>a:
    print("the input value is greater then the actual value")
  else:
    print("enter value is lesser than the actual value")
  k+=1
else:
 print("you lose buddy the actual value is ",a)
