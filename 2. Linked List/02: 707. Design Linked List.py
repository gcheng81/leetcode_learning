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
