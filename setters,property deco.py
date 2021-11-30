# class employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#
#     # def email(self):
#     #     return (f"{self.fname}.{self.lname}@gmail.com")
#
#     @property
#     def email(self) :
#         if self.fname==None or self.lname==None:
#            return ("email is not set")
#
#         else:
#          return (f"{self.fname}.{self.lname}@gmail.com")
#
#
#     # format-@<fun want to set>.setter
#
#     @email.setter
#     def email(self,string):
#         names=string.split("@")[0]
#         self.fname=names.split(".")[0]
#         self.lname = names.split(".")[1]
#
#
#
#     @email.deleter
#     def email(self):
#         self.fname=None
#         self.lname=None
#
# samrat=employee("Samrat","mishra")
#
# # now i can call my email func
# # print(samrat.email())   #after makin prop deco i cannot use this
#
# # but if i use my email without brac it give me location
# print(samrat.email)  #so i have to make a prop decorator
#
# # samrat.fname= 'ram'
# # print(samrat.email)
#
# # now let i have to do
# # samrat.email=rahul.kapoor@gmail.com     it will give me error so ,to do this i make a setter for email
#
# samrat.email="samrat.kapoor@gmail.com"
# print(samrat.email)
#
# del samrat.email
# print(samrat.email)


# ____________________________________________________________________________

