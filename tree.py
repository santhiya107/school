class tree:
   def __init__(self, data):
      self.data= data
      self.lc =None
      self.rc =None
   def insert(self,data):
      if self.data is None:
         self.data = data
         return
      if self.data ==data:
         return
      if self.data > data:
         if self.lc:
            self.lc.insert(data)
         else:
            self.lc=tree(data)
      else:         
         if self.rc:
            self.rc.insert(data)
         else:
            self.rc=tree(data) 
   def minValue(self):
        current = self 
        while(current.left is not None):
            current = current.left
        return current  
   def delete(self,data):
      if self.data is None:
         print("empty tree")  
         return
      if self.data >data:
         if self.lc:
            self.lc=self.lc.delete(data)  
         else:
            print("the value is not present in the tree")
      if self.data < data:
         if self.rc:
            self.rc=self.rc.delete(data)
         else:
            print("value not present")
      else:            
         if self.lc is None:
            temp=self.rc            
            self=None
            return temp
         elif self.rc is None:
            temp=self.lc            
            self=None            
            return temp
              
         temp = self.minValue(self.right)
         self.data = temp.data        
         self.right = self.delete(self.right, temp.data)
          
               
   def preorder(self):
      print(self.data,end=" ")
      if self.lc:
         self.lc.preorder() 
      if self.rc:
             self.rc.preorder()       
   def inorder(self):
      if self.lc:
         self.lc.preorder()
      print(self.data,end=" ")
      if self.rc:
         self.rc.preorder()     
   def postorder(self):
      if self.lc:
             self.lc.preorder() 
      if self.rc:
             self.rc.preorder()                     
      print(self.data,end=" ")                   
            
root=tree(15)
l=[9,40,3,5,39,51]
for i in l:
   root.insert(i)


#print("Preorder traversal:\n ")
#root.preorder()
#print("\n")
#print("Postorder traversal:\n ")
#root.postorder()
#print("\n")
#print("Inorder traversal:\n ")
root.inorder()
root.delete(51)
print("\nafter deletion:\n")
root.inorder()