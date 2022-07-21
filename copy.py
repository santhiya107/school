class tree:
   def __init__(self, data):
      self.data= data
      self.lc =None
      self.rc =None
   def insert(root,data):
      if root.data is None:
         root.data = data
         return
      if root.data ==data:
         return
      if root.data > data:
         if root.lc:
            root.lc.insert(data)
         else:
            root.lc=tree(data)
      else:         
         if root.rc:
            root.rc.insert(data)
         else:
            root.rc=tree(data) 
   def minValue(root,data):
        current = data   
        while(current.left is not None):
            current = current.left
        return current  
   def delete(root,data):
      if root.data is None:
         print("empty tree")  
         return
      if root.data >data:
         if root.lc:
            root.lc=root.lc.delete(data)  
         else:
            print("the value is not present in the tree")
      if root.data < data:
         if root.rc:
            root.rc=root.rc.delete(data)
         else:
            print("value not present")
      else:
         if root.lc is None:
            temp=root.rc
            root=None
            return temp
         elif root.rc is None:
            temp=root.lc
            root=None
            return temp
              
         temp = root.minValue(root.right)
         root.data = temp.data        
         root.right = root.delete(root.right, temp.data)
          
               
   def preorder(root):
      print(root.data,end=" ")
      if root.lc:
         root.lc.preorder() 
      if root.rc:
             root.rc.preorder()       
   def inorder(root):
      if root.lc:
         root.lc.preorder()
      print(root.data,end=" ")
      if root.rc:
         root.rc.preorder()     
   def postorder(root):
      if root.lc:
             root.lc.preorder() 
      if root.rc:
             root.rc.preorder()                     
      print(root.data,end=" ")                   
            
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