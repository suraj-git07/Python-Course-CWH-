def gcd(a,b):
    if a<b:
        print("a have to grater than b")
        return
    elif b == 0:

        return a
    else:
        return gcd(b,a%b)

# main

a,b=input("enter a,b").split(",")
a,b=int(a),int(b)
result=gcd(a,b)
print("THE RESULT OF GCD:",result)

