# java script object notation
# Json is a data exchange format similar to XML

# first to craet address book and write some records into it
# read this book

# /json is just a concept/ not a actual object in python, it is used to trasfer data
# json file ext=.json
# json is a text but can accept various data types=numbers,str,boolean,arrays,dict,null
# data types json not allowed=func,date,undefined

# initially we are making a dic and convert it in json string


book={}
book["bob"]={"name":"tom","class":"tenth","school":"sslt gujrat"}
book["ram"]={"name":"ram","class":"ninth","school":"spring field"}

print(book)
print(type(book))

# now to tranfer the data i am changing it into string or json format

import json
s=json.dumps(book)
print(s)
print(type(s))
# now i ad this to a file
# with open("myjson","w") as f:
#     f.write(s)

# now to convert json to dict use loads
d=json.loads(s)
print(d)
print(type(d))
