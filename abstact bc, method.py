# abstract base class is a class where the class contains some basic rules which would be followed by the class inhereted by it
# abstract method is used to setup those rules

# from abc import ABC ,abstractmethod  #importation
#
# # now i wnt to make a base class where there is a rule thar every inhereted class should have a print area func
#
# class shape(ABC):
#     @abstractmethod
#     def printarea(self):
#         return 0
# # you  con not make objects of abstract base class
#
# class rectange(shape):
#     # now rectange should have printarea
#      def __init__(self):
#          self.length=4
#          self.breadth=6
#
#      def printarea(self):
#          print(f"area is {self.length * self.breadth}")
# abc=rectange()
# print(abc.length) #here it give error because there is no printarea till now
#
# # now no error
#
# print(abc.printarea())
#
#
