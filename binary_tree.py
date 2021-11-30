
#binary tree implementation
#search time complexity , space complexity :O(log n )


class binary_tree_node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def add_child(self, data):
        if data == self.data :
            return

        if data < self.data:

            if self.left :

               self.left.add_child((data))

            else:
                self.left = binary_tree_node(data)
                
        if data > self.data:

            if self.right :

               self.right.add_child((data))

            else:
                self.right = binary_tree_node(data)



    def inorder_traversal(self):
        elements = []
        #for elements in left subtree

        if self.left:
            elements+= self.left.inorder_traversal()

        # for base node

        elements.append(self.data)

        #for right subtree

        if self.right:
            elements+= self.right.inorder_traversal()

        return elements


    def postorder_traversal(self):
        elements =[]
        # for elements in left subtree

        if self.left:
            elements+= self.left.postorder_traversal()

        #for element in right subtree

        if self.right:
            elements+= self.right.postorder_traversal()

        #for the base node

        elements.append(self.data)

        return elements

    def search_tree(self,value):
        if value == self.data:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search_tree(value)
            else:
                return False

        else:
            if self.right:
                return self.right.search_tree(value)
            else:
                return False


def bulid_tree(arr):
    root = binary_tree_node(arr[0])
    for i in range(1,len(arr)):
        root.add_child(arr[i])

    return root


if __name__=="__main__":

    arr = [10,6,7,4,3,2,5,1,8,9]

    bintree = bulid_tree(arr)

    #print(bintree.inorder_traversal())

    #print(bintree.postorder_traversal())
    print(bintree.search_tree(2))





