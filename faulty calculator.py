# faulty calculator
a=(input("enter the first number \n"))
b=(input("enter the second number \n"))
print("enter the operator as per the sepcific details ")
print(" '*' for multiplycation, '/' for division,'+' for addition")
operator=input("enter the operator as per above details")
if operator not in [ "*","/","+"]:
    print("you entered a wrong operator !!!")
else:
    operation= a+operator+b
    if operation=="45*3":                  # 45*3=555
       print( "answer is :",555)
    elif operation=="59+9":                  # 45*3=555, 56+9=77,56/6=4
       print( "answer is :",77)
    elif operation =="56/6":
       print("answer is :",4)
    else:
        if operator=="*":
           print("answer is:",int(a) * int(b))
        elif operator=="+":
           print("answer is:",int(a) + int(b))
        else:
           print("answer is:",int(a) / int(b))

