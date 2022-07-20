"https://leetcode.com/problems/reverse-linked-list-ii/"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head
        # find the predecessor of the left position
        left_pre = dummy_node
        for _ in range(left-1):
            left_pre = left_pre.next
        left_cur = left_pre.next
        
        pre = left_pre
        cur = left_cur
        for _ in range(right-left+1):
            # save
            tmp = cur.next
            # reverse
            cur.next = pre
            # move
            pre = cur
            cur = tmp
        
        left_pre.next = pre
        left_cur.next = cur
        
        return dummy_node.next
        
