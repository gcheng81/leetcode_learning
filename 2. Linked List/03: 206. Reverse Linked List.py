"https://leetcode.com/problems/reverse-linked-list/"


# Solution 1: Two Pointers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        
        while(cur):
            # 1) save the successor of the cur_node
            succ = cur.next
            # 2) reverse
            cur.next = pre
            # 3) move two pointers
            pre = cur
            cur = succ
        return pre
            
        
# Solution 2: Recursion
