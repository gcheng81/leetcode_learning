“https://leetcode.com/problems/swap-nodes-in-pairs/”

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0, head)
        cur = dummy_head
        
        while(cur.next and cur.next.next):
            # save
            tmp1 = cur.next
            tmp2 = cur.next.next
            tmp3 = cur.next.next.next
            # swap (把后三个node都保存下来，这样先连哪个，顺序完全没关系)
            cur.next = tmp2
            tmp2.next = tmp1
            tmp1.next = tmp3
            # move pointer
            cur = cur.next.next
            
        return dummy_head.next
