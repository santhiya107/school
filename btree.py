class Node:
    def __init__(self, data=None):
      self.data= data
      self.lc =None
      self.rc =None
class tree:
   def __init__(self):
      self.root = None
   def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self.insert(self,self.root)
   def insertn(self,data,temp):
        if data < temp.data:
            if temp.lc is None:
                temp.lc=Node(data)    
            else:
                self.insertn(data,temp.left) 
        elif data > temp.data:
            if temp.rc is None:
                temp.rc=Node(data)    
            else:
                self.insertn(data,temp.left) 
        else:
            print("node value is already present in the tree")
