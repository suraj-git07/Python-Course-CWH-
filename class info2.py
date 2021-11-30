class samratltd:  # format class <classname>: block take the specifications
    # constructor concept
    # intiall samratltd takes no argument
    no_leaves=10
    def __init__(self, aname, arole, acode):  # constructor allows me to add arguments to my class object
        self.name = aname
        self.role = arole
        self.code = acode


    # class method is atype of decorator which is used to access the instances of a class it takes class as an argument
    @classmethod
    def change_leaves(cis,leaves_wt):
       cis.no_leaves=leaves_wt




harry=samratltd("suraj",'director',7)
print(harry.no_leaves)
# now i am going to chnge leaves of class instance
harry.change_leaves(14)
print(harry.no_leaves)
