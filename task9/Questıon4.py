class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class LinkedList: 
  
    def __init__(self): 
        self.head = None
  
    def reverse(self): 
        prev = None 
        current = self.head 
        
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        
        self.head = prev 
          
    def push(self, new_data): 
        new_node = Node(new_data) 
        new_node.next = self.head 
        self.head = new_node 
  
    def printList(self): 
        temp = self.head 
        while(temp): 
            print(temp.data, end = ' ') 
            temp = temp.next
        print()
  
  
ll = LinkedList() 
ll.push(20) 
ll.push(4) 
ll.push(15) 
ll.push(85)

ll.printList() 
ll.reverse() 
ll.printList()