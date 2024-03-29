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
            if pre.val == cur.val: # 如果相等，则pre不动，只移动cur
                pre.next = cur.next
                cur = cur.next
            else: # 如果不等，则pre和cur都向前移动一位
                pre = pre.next
                cur = cur.next
        return dummy_head.next

    
# easier to understand
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode(0, head)
        slow = head
        fast = head.next
        
        while fast:
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val
            fast = fast.next
        # Disconnect from the following repeated elements
        slow.next = None
        return dummy.next
    
 
