"https://leetcode.com/problems/design-linked-list/"

# Solution 1: Single Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.dummy_head = Node(0) #virtual head node
        self.size = 0 # number of nodes
        
    def get(self, index: int) -> int:
        # note here is >=, cuz index is [0, size-1] 
        if index<0 or index>=self.size:
            return -1
        cur_node = self.dummy_head # begin from virtual head node
        for _ in range(index+1): # traverse linked list to the index
            cur_node = cur_node.next
        return cur_node.val
    
    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
    
    def addAtIndex(self, index: int, val: int) -> None:
        # If index is negative, the node will be inserted at the head of the list.
        if index < 0:
            index = 0
        # If index is greater than the length, the node will not be inserted.
        elif index > self.size:
            return
          
        # If index is equal to the length, the node will be inserted to the tail
        # 1) find predecessor of the node to be added
        pre_node = self.dummy_head
        for _ in range(index):
            pre_node = pre_node.next
        # 2) initialize node to be added
        new_node = Node(val)
        # 3) insert the new node
        new_node.next = pre_node.next
        pre_node.next = new_node
        self.size += 1
    
  
    def deleteAtIndex(self, index: int) -> None:
        # note here is >=, cuz index is [0, size-1] 
        if index<0 or index>=self.size:
            return
        
        # 1) find predecessor of the node to be deleted
        pre_node = self.dummy_head
        for _ in range(index):
            pre_node = pre_node.next
        # 2) delete the node
        del_node = pre_node.next
        pre_node.next = del_node.next
				self.size -= 1
        

# Your MyLinkedList object will be instantiated 实例化 and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)




# Solution 2: Doubly Linked List
class Node:
    def __init__(self, val):
        self.val = val
        self.pre = None
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.dummy_head = Node(0)
        self.dummy_tail = Node(0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.pre = self.dummy_head

    def get(self, index: int) -> int:
        if index<0 or index>=self.size:
            return -1
        
        if index < self.size-1-index: # index ahead
            cur_node = self.dummy_head
            for _ in range(index+1): # 取到
                cur_node = cur_node.next
        else:
            cur_node = self.dummy_tail
            for _ in range(self.size-index): # 取到
                cur_node = cur_node.pre
        return cur_node.val
                

    def addAtHead(self, val: int) -> None:
        # find the predecessor and successor of the new node
        pred = self.dummy_head
        succ = self.dummy_head.next
        
        # initilize the new node
        new_node = Node(val)
        
        # add
        new_node.pre = pred
        new_node.next = succ
        pred.next = new_node
        succ.pre = new_node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        # find the predecessor and successor of the new node
        pred = self.dummy_tail.pre
        succ = self.dummy_tail
        
        # initilize the new node
        new_node = Node(val)
        # add
        new_node.pre = pred
        new_node.next = succ
        pred.next = new_node
        succ.pre = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index<0:
            index = 0
        elif index>self.size:
            return
        
        # 1) find the predecessor and successor of the new node
        if index < self.size-1-index:
            pre_node = self.dummy_head
            for _ in range(index): # 取不到
                pre_node = pre_node.next
            next_node = pre_node.next
        else:
            next_node = self.dummy_tail
            for _ in range(self.size-index): # 取到
                next_node = next_node.pre
            pre_node = next_node.pre
        
        # 2) initilize the new node
        new_node = Node(val)
        # 3) add
        new_node.next = next_node
        new_node.pre = pre_node
        pre_node.next = new_node
        next_node.pre = new_node
        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index<0 or index>=self.size:
            return
        
        # 1) find the predecessor and successor of the node to be deleted
        if index < self.size-1-index:
            pre_node = self.dummy_head
            for _ in range(index): # 取不到
                pre_node = pre_node.next
            next_node = pre_node.next.next
        else:
            next_node = self.dummy_tail
            for _ in range(self.size-1-index): # 取不到
                next_node = next_node.pre
            pre_node = next_node.pre.pre
        
        # 2) delete
        pre_node.next = next_node
        next_node.pre = pre_node
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
