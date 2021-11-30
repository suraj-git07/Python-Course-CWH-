def fib(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)


# main
till=int(input("enter till which number you want fibonacci"))
for i in range(1,till+1):
    print(fib(i),end=" ")


