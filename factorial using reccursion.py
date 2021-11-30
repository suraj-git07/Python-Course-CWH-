n=int(input("enter the number whose factorial you want"))

def factorial_recursive(n):
    if n==1:
        return 1
    else:
       return n*factorial_recursive(n-1)
print(f"factorial of {n} ={factorial_recursive(n)}")