class Node:
   def __init__(self, data=None):
      self.data= data
      self.next =None
      self.prev =None
class Linkedlist:
   def __init__(self):
      self.head = None

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
            val= val.prev
   def add_empty(self,data):
       if self.head is None:
           n=Node(data)
           self.head=n
       else:
           print("list is not empty")
   def add_begin(self,data):
       n=Node(data)
       if self.head is None:
           self.head=n
       else:
           n.next=self.head
           self.head.prev=n
           self.head=n
   def add_end(self,data):
       n=Node(data)
       if self.head is None:
           self.head=n
       else:
           temp=self.head
           while temp.next is not None:
               temp=temp.next
           temp.next=n
           n.prev=temp
   
   def add_after(self,data,x):
       if self.head is None:
           print("empty list")
       else:
           temp=self.head
           while temp is not None:
               if x==temp.data:
                    break
               temp=temp.next
           if temp is None:
               print("node not present")
           else:
               n=Node(data)
               n.next=temp.next
               n.prev=temp
               n.next.prev=n
               temp.next=n
   def add_before(self,data,x):
       if self.head is None:
           n=Node(data)
           self.head=n  
       else:
           
           temp=self.head
           while temp is not None:
               if x==temp.data:
                    break
               temp=temp.next
           n=Node(data)
           n.next=temp
           n.prev=temp.prev
           temp.prev.next=n
           temp.prev=n
       
            
   def search(self,x):
       if self.head is None:
           print("list empty")
       else:
           if x==self.head.data:
               print("element is present in the list")
           else:
               temp=self.head
               temp=temp.next
               if x==temp.data:
                   print("element is present in the list")
               else:
                   print("element not present in list")
       
                   
   def del_begin(self):
       if self.head is None:
           print("list empty")
       else:
           self.head=self.head.next
   def del_begin(self):
       if self.head is None:
           print("list empty")
       else:
           if self.head.next is None:
               self.head=None
               print("list empty after delete node")
           else:
               self.head=self.head.next
               self.head.prev=None
   def del_end(self):
       if self.head is None:
           print("list empty")
       else:
           if self.head.next is None:
               self.head=None
               print("list empty after delete node")
              
           else:
               temp=self.head
               while temp.next is not None:
                   temp=temp.next
               temp.prev.next=None
   def del_val(self,x):
       if self.head is None:
           print("list empty")
           return
       if self.head.next is None:
           if x==self.head.data:
               self.head=None
           else:
               print("value is not present in the list")
           return
       if self.head.data==x:
           self.head=self.head.next
           self.head.prev=None
           return
       temp=self.head
       while temp.next is not None:
           if x==temp.data:
               break
           temp=temp.next
       if temp.next is not None:
           temp.next.prev=temp.prev
           temp.prev.next=temp.next
       else:
           if temp.data==x:
               temp.prev.next=None
           else:
               print("value is not present in list")
       
           
       
       
l=Linkedlist()
#l.add_empty(50)
l.add_begin(23)
l.add_end(100)
l.add_after(34,23)
l.add_before(90,100)

#l.add_pos(80,4)
#l.del_begin()
#l.del_end()
#l.del_val(60)
#l.search(60)
l.printlist()
print("\nlist in reverse order :")
l.printlist_reverse()
