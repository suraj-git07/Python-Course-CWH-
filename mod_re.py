# a regular expression is a search text string for describing a search pattern
import re
# Nameage = '''                                         #just an example
# Janice is 22 and Theon is 33
# Gabriel is 44 and Joey is 21
# '''
#
# ages = re.findall(r"\d{1,3}",Nameage)
# names = re.findall(r"[A-Z][a-z]*",Nameage)
#
#
# agedict={}
#
# x=0
#
# for eachnames in names:
#     agedict[eachnames] = ages[x]
#     x += 1
#
# print(agedict)

# ------------------------------------------------------------------
# re.search

# if re.search("inform", "we need to inform  him with the latest information"):
#
#     print("there is inform")

# re.findall
#
# allinform = re.findall("inform","we need to inform  him with the latest informatiom")       #it will give us a list containing all the matches
#
# print(allinform)

# re.finditer

# str="we need to inform  him with the latest information"
#
# for i in  re.finditer("inform", str):
#     loctus = i.span()
#
#     print(loctus)


# ------------------------------------------------------------match words with pattern-----------------

# str = "Sat,hat,mat,pat"

# allstr = re.findall(r"[Shmp]at",str)
#
# print(allstr)

# ------------------------------------------------------------------match series of range of character----------------------------

# str = "Sat,hat,mat,pat"

# allstr = re.findall(r"[h-m]at",str)
# for everythig apart for above range
# allstr = re.findall(r"[^h-m]at",str)
# print(allstr)

# ---------------------replace a str--------------------

#
# food = 'hat rat mat pat'
#
# # making pattern obj alows us t use more func like 'sub'
#
# regex=re.compile(r'[r]at')
#
# food=regex.sub("food",food)
#
# print(food)

# ________________________match a single character______

# randstr = '12345'
# print("matches",len(re.findall("\d{5}",randstr)))                #\d search any number  and than {range}
# print("matches",len(re.findall("\d{5,10}",randstr)))                #\d search any number  and than {range}
#


# \w= [a-zA-z0-9_]

#  \W = [^a-zA-z0-9_]


# ---------------------validating phone number-------------------
# general order ==  nnn-nnn-nnnn

# numbers = {"ph":" 444-445-1234" , "ph2" : "111-1111-1113"}
#
# for key , value in numbers.items() :
#
#    if re.search(r"\w{3}-\w{3}-\w{4}", value):
#          pass
#    else:
#        print(f"{key} is not a number")



# \s= [\n\f\r\t\v]
#
# \S=[^\n\f\r\t\v]

