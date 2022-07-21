"https://leetcode.com/problems/remove-nth-node-from-end-of-list/"

# Solution 1: One Pointer

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1
        """
        # edge case 1: 
        if size == 1 and n==1:
            return
        """
        index = size - n
        """
        # edge case 2: node to be removed is the first node from front of the list
        if index == 0: 
            dummy_head.next = head.next
        else:
            pre = head
            for _ in range(index-1):
                pre = pre.next
            pre.next = pre.next.next
        """
        pre = dummy_head
        for _ in range(index):
            pre = pre.next
        pre.next = pre.next.next
        
        return dummy_head.next
   
  
  
# Solution 2: Two Pointers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        fast = dummy_head
        slow = dummy_head
        
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return dummy_head.next
        
