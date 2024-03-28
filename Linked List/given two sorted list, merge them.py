# A complete working Python program to merge two sorted
# linked lists
  
# Node class 
  
  
class Node: 
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
    # This function is in LinkedList class. It inserts 
    # a new node at the beginning of Linked List. 
  
    def push(self, new_data): 
  
        # 1 & 2: Allocate the Node & 
        #     Put in the data 
        new_node = Node(new_data) 
  
        # 3. Make next of new Node as head 
        new_node.next = self.head 
  
        # 4. Move the head to point to new Node 
        self.head = new_node 


  
    # merge two sorted LL 
    def getmerge(self,a,b):
    
        if a == None :
          return b
        if b == None:
          return a
          
        if a.data < b.data:
          head = a
          last = a
          a = a.next
        else:
          head = b
          last = b
          b = b.next
        

        # merge lists
      while(a!= None and b!= None):
        
        if a.data < b.data:
          last.next = a
          last = a
          a = a.next
        else:
          last.next = b
          last = b
          b = b.next

      if a is None:
        last.next = b
      if b is None:
        last.next = a
      return head
           
        # if we get to this line, the caller was asking 
        # for a non-existent element so we assert fail 
        assert(false) 
        return 0
  
  
# Driver Code 
if __name__ == '__main__': 
  
    llist1 = LinkedList() 
    # Use push() to construct below list 
    # 1->12->7 
    llist1.push(1) 
    llist1.push(4) 
    llist1.push(7) 
    llist1.push(10)
    

    llist2 = LinkedList() 
    # Use push() to construct below list 
    # 2->5->8 
    llist2.push(2) 
    llist2.push(5) 
    llist2.push(8) 
  
    
    print("Merged list is :", llist.getmerge(llist1,llist2)) 

# Output: Merged list is 1
# Time Complexity: O(n)
# Auxiliary Space: O(1) space created for variables
