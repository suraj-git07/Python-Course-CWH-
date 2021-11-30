class A:
    classvar1=23
    def __init__(self):
        self.var="name"
        self.var1="class"

        # my first class
# format of searching varables ,instance varaible of object class -instance variable of inherited class- class variable of object class -class variable of inherited class
# if there is a func,att of same  name (inherited with one ) in two classes the object class override the inherted func ,att

class B(A):
    def __init__(self):
        # self.var="bname"
        # self.var1='bclass'
        super().__init__()     #here super method call my super file constructor
        # self.var = "bname"
        # self.var1='bclass'


sam=B()

print(sam.var1)