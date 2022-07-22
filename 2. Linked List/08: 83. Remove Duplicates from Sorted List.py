"https://leetcode.com/problems/remove-duplicates-from-sorted-list/"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        if head is None:
            return head
        pre = head
        cur = head.next
        
        while cur:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = cur.next
            else:
                pre = pre.next
                cur = cur.next
        return dummy_head.next
