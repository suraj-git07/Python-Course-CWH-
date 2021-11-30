# whenever we try use add some no we use + operator but at background a method as , __add__()  , is running
# and same  for all the operator is is a method these methods is known asspecial or magic methods or dundder method

# print(5+6)
# print(  int.__add__(5,6))  #int =type
#
# # for multiplycation
# print(int.__mul__(5,6))

class samratltd:
    def __init__(self,aname,arole,acode):
        self.name=aname
        self.role=arole
        self.code=acode
    def __add__(self,other):
        return self.code+ other.code

samrat=samratltd("samrat","coader",7)
rohan=samratltd("rohan","cleaner",45)
# print(samrat.code)
# print(rohan.code)

# let i write
# print(samrat+rohan)   #it give me error since here python confuses
#  so
print(samrat+rohan)

# that how i can overlode any operator