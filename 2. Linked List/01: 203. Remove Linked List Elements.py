"https://leetcode.com/problems/remove-linked-list-elements/"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_head  = ListNode(0, head)
        cur = dummy_head
        while cur.next != None:
            if cur.next.val==val:
                cur.next = cur.next.next
            else:
                cur = cur.next #移向下一个node
        return dummy_head.next
        
