class Node:
   def __init__(self, data):
      self.data= data
      self.next =None
      self.prev =None
class Linkedlist:
   def __init__(self):
      self.head = None
      self.tail=None

   def printlist(self):
        val= self.head
        while val is not None:
           print(val.data ,"-->", end=" ")
           val= val.next
   def printlist_reverse(self):       
        val= self.head        
        while val.next is not None:
            val=val.next
        while val is not None:
            print(val.data ,"-->", end=" ")
  
   def add_begin(self,data):
       n=Node(data)
       self.head=n
       self.tail=n
       n.next=self.head
       if self.head is not None:
           while temp.next !=self.head:
               temp=temp.next
           temp.next=n
       n.next=n
       self.head=n
            
               
            
  
       
l=Linkedlist()

l.add_begin(23)

print(l.head.prev.data)
#l.printlist()
#print("\nlist in reverse order :")
#l.printlist_reverse()
