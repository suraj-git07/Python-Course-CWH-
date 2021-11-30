# raise  keyword is used to generate exception  as per programmer will
# you can raise the excep. based on some condition also ,



name=input("enter your name")

if name.isnumeric():
    raise Exception("numbers are not allowed ")     #kuch bhi str daal lo

else:
    print(f"hello {name}")


# you can also run a specific Exception like eol ,value error etc
