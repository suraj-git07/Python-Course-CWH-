# class library:
#
#     def __init__(self,libname,listofbooks):
#         self.name=libname
#         self.booklist=listofbooks
#         self.lenders={}
#
#     def donate(self,namebook):
#         self.booklist.append(namebook)
#         print("your book is added")
#         return self.booklist
#
#     def lend(self,book,name):
#        if book in self.booklist:
#           self.booklend=book
#           self.booklist.remove(book)
#           self.lender=name
#           a={self.booklend:self.lender}
#           print("please return the book after you read")
#           return self.lenders.update(a)
#
#        elif book in self.lenders:
#            print(f"sorry book is not available at this time book is lended by {self.lenders[book]} ")
#        else:
#             print("sorry we dont have this book")
#
#
#     def giveback(self,book,name):
#         self.lender=name
#         if book in self.lenders and  self.lenders[book]==self.lender:
#
#             del self.lenders[book]
#             self.booklist.append(book)
#             print("we got our book back ,thank you ")
#
#
#         elif book in self.lenders:
#             print("this book is not lended by you")
#         else:
#             print("your given information is incorrect")
#
#
# if __name__ == '__main__':
#   samratlib=library("samratlibrary",["panchtatra","ramayan","harry potter","iron_man"])
# while True:
#     try:
#         task=input("what you have to do donate,lend,giveback or nothing")
#
#         if task=="nothing" :
#            break
#         elif task=="donate":
#            book=input("enter the book which you want to donate")
#            samratlib.donate(book)                           #let there is only one library
#         elif task=="lend":
#            name=input("please enter you name")
#            book=input("please enter the book which you want to lend")
#            samratlib.lend(book,name)
#
#         elif task=="giveback":
#            name = input("please enter you name")
#            book = input("please enter the book which you want to give back")
#            samratlib.giveback(book,name)
#         else:
#             print("you entered a wronge input")
#     except:
#         print("sorry something happend")



