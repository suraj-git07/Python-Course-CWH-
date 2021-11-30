
#implementation  of trees

class treenode():
    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None


    def add_child(self,child):
        child.parent = self
        self.child.append(child)


    def give_level(self):
        level = 0
        P = self.parent
        while P:
            level +=1
            P = P.parent

        return level  
    

    def print_tree(self, input_level):
        space = self.give_level()    #also used to check level       



        if self.parent :
            string = "             " *space + "|__"     #just to spacing strcture
        else:
            string = ""


        if space <= input_level:                        
            print(string + self.data)
            if len(self.child):
                for child in self.child:
                    child.print_tree(input_level)
                



def buildtree():
    root = treenode("Electronics")

    laptop = treenode("laptop")


    laptop.add_child(treenode("Dell"))
    laptop.add_child(treenode("HP"))
    laptop.add_child(treenode("Mac"))


    TV = treenode("TV")

    TV.add_child(treenode("Samsung"))
    TV.add_child(treenode("MI"))
    TV.add_child(treenode("LG"))


    Smartphone = treenode("Smartphone")


    Smartphone.add_child(treenode("Vivo"))
    Smartphone.add_child(treenode("Iphone"))
    Smartphone.add_child(treenode("Nokia"))


    root.add_child(laptop)
    root.add_child(TV)
    root.add_child(Smartphone)

    return root


if __name__ == "__main__":

    root = buildtree()
    
    
    root.print_tree(1)
