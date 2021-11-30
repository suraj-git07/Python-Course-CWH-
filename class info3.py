class samratltd:

    no_leaves=10
    def __init__(self, aname, arole, acode):  # constructor allows me to add arguments to my class object
        self.name = aname
        self.role = arole
        self.code = acode

    # here we are going to make a static method
    # static func is atype of class method which nither take self as an argumment nor cis
    @staticmethod
    def print_good():
        print("samrat is a good coader")

        # now i can use thus func for either me instance or for my class

harry=samratltd("suraj",'director',7)
# print(harry.no_leaves)
# # now i am going to chnge leaves of class instance
# harry.change_leaves(14)
# print(harry.no_leaves)
print(harry.print_good())