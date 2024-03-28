# A complete working Python program to find second last node 
# in a linked list 
  
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
  
    # Returns data at last node in linked list 
    def getseclast(self): 
        current = self.head  # Initialise current 
        if current == None or current.head==None:
          return

        # Loop while end of linked list is not reached 
        while (current.next.next != None): 
            current = current.next 
        return current.data 
           
        # if we get to this line, the caller was asking 
        # for a non-existent element so we assert fail 
        assert(false) 
        return 0
  
  
# Driver Code 
if __name__ == '__main__': 
  
    llist = LinkedList() 
  
    # Use push() to construct below list 
    # 1->12->1->4->1 
    llist.push(1) 
    llist.push(4) 
    llist.push(1) 
    llist.push(12) 
    llist.push(1) 
  
    
    print("Element at second last is :", llist.getseclast()) 

# Output: Element at last is 4
# Time Complexity: O(n)
# Auxiliary Space: O(1) space created for variables
