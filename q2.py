class Node:
    def __init__(self, data):
        self.data= data
        self.lc= None
        self.rc = None
    
    def preorder(self):
        print(self.data, end=' ')
        if self.lc:
            self.lc.preorder()
        if self.rc:
            self.rc.preorder()
    def inorder(self):
        if self.lc:
            self.lc.inorder()
        print(self.data, end=' ')
        if self.rc:
            self.rc.inorder()
    def postorder(self):
        if self.lc:
            self.lc.postorder()
        if self.rc:
            self.rc.postorder()
        print(self.data, end=' ')


root = Node(1)
root.lc=Node(2)
root.lc.lc=Node(4)
root.lc.lc.lc=Node(8)
root.lc.lc.rc=Node(9)
root.lc.rc=Node(5)
root.lc.rc.lc=Node(10)
root.lc.rc.rc=Node(11)
root.rc=Node(3)
root.rc.lc=Node(6)
root.rc.lc.rc=Node(13)
root.rc.rc=Node(7)
root.rc.rc.rc=Node(14)
print("Preorder Traversal: ", end="")
root.preorder()
print("\nInorder Traversal: ", end="")
root.inorder()
print("\nPostorder Traversal: ", end="")
root.postorder()
