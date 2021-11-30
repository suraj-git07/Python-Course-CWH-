#Hash maps
#python implementation - Dictionary

class Hashmap():
    def __init__(self):
        self.max = 1000
        self.arr = [[] for i in range(self.max)]


    def gethash(self,key):
        h = 0
        for i in key:
            h+=ord(i)
        return h


    def __setitem__(self,key,value):

        h = self.gethash(key)
        found = False
        for  idx,element in enumerate(self.arr[h]):
            if element[0] == key:
               self.arr[h][idx] =(key, value)
               found = True
               break
        if not found:    
            self.arr[h].append((key,value))
         
    
    def __getitem__(self, key):
        h = self.gethash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]
            
    def __delitem__(self,key):

        h= self.gethash(key)
        del self.arr[h]


if __name__=="__main__":

    table = Hashmap()

    table["march 8"] = 310
    table["march 7"] = 420    
    table["march 6"] = 7
    table["march 17"] = 345

    table["march 6"] =10

    print(table.arr)

    
    print(table["march 6"])
    print(table["march 17"])
    
    del table["march 7"]
    print(table.arr)
