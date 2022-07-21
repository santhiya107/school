class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder(root):
    if root is not None:        
        inorder(root.left)        
        print(str(root.data) + "->", end=' ')        
        inorder(root.right)
def preorder(root):
    if root is not None: 
        print(str(root.data) + "->", end=' ')            
        preorder(root.left)           
        preorder(root.right)
def postorder(root):
    if root is not None:        
        postorder(root.left)           
        postorder(root.right)
        print(str(root.data) + "->", end=' ')    
def insert(node, data):    
    if node is None:
        return Node(data)
    if data < node.data:
        node.left = insert(node.left, data)
    else:
        node.right = insert(node.right, data)
    return node
def minValue(node):
    current = node    
    while(current.left is not None):
        current = current.left
    return current
def delete(root, data):    
    if root is None:
        return root    
    if data < root.data:
        root.left = delete(root.left, data)
    elif(data > root.data):
        root.right = delete(root.right, data)
    else:    
        if root.left is None:
            temp = root.right
            
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp     
        temp = minValue(root.right)
        root.data = temp.data        
        root.right = delete(root.right, temp.data)
    return root

root = None
# root = insert(root, 8)
# root = insert(root, 3)
# root = insert(root, 1)
# root = insert(root, 6)
# root = insert(root, 7)
# root = insert(root, 10)
# root = insert(root, 14)
# root = insert(root, 4)
l=[15,9,40,3,5,51]
for i in l:
   root=insert(root,i)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\n")
root = delete(root,51)
print("Inorder traversal: ", end=' ')
inorder(root)
print("\npreorder traversal:")
preorder(root)
print("\npostorder traversal:")
postorder(root)