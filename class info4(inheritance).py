''' inheritance is basically a concept where we use the function and methods of a
 preexisting calss in a new class  without actually writing it again'''
#
# class samratltd:  # format class <classname>: block take the specifications
#     # constructor concept
#     # intiall samratltd takes no argument
#     no_leaves=10
#     def __init__(self, aname, arole, acode):  # constructor allows me to add arguments to my class object
#         self.name = aname
#         self.role = arole
#         self.code = acode
#
#     def printdetails(self):
#         print(f"name of employee is {self.name},role is {self.role},code is {self.code}")
#
#     # class method is atype of decorator which is used to access the instances of a class it takes class as an argument
#     @classmethod
#     def change_leaves(cis,leaves_wt):
#        cis.no_leaves=leaves_wt
#

# new class
# class samratlab(samratltd):
#     # now i can class the same methods or func in samratltd in objects of samratlab
#     def __init__(self,aname,arole,acode,aage):
#         # here constructure of both class is diff
#         # till i ot made it i can use my previous init here also
#         self.name = aname
#         self.role = arole
#         self.code = acode
#         self.age  = aage
#     def printdetails(self):
#         print(f"name of employee is {self.name},role is {self.role},code is {self.code}, age is {self.age}")

# it is a type of single inheritance means ,one class is inherited in one class

#
# harry=samratltd("suraj",'director',8)
# rohan=samratltd("rohan","maneger",14)
#
# # rohit=samratlab("rohit","programmer",12,21)
# suraj=samratlab("suraj","boss",7,16)



# multiple inheritance
# initially i only have one class samratltd
#
# class player:
#     def __init__(self,aname,game):
#         self.name=aname
#         self.game=game
#
#     def printdetails(self):
#         print(f"name of player is {self.name},game is {self.game}")


#
#
# sohan=player("sohan",'cricket')
# vijay=player("vijay","football")
#
#
# class cool_samratltd(samratltd,player):  #now inthis class i can us ethe attribute s of both samratltd and player
#     pass
#
# # here the init in cool_samratltd is got from the first inherter(samratltd ) and if thre are to func that are of same name of prefrence func is one first inheretor
#
#
# ram=cool_samratltd("ram","player",2)
# print(ram.printdetails())


# -------------------------------------------------------------------------------


#
class A:
    def __init__(self):
        self.game="game"
        self.name="name"
        super().__init__()

    def __add__(self,other):
        return self.game+other.name


class B:
    def __init__(self):
        self.fame="fame"
        self.lame="lame"
        super().__init__()

class C(B,A):
    def __init__(self):
        self.chain="chain"
        super().__init__()


man=C()
print(man.fame)
print(man.__add__(man))