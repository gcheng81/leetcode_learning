"https://leetcode.com/problems/linked-list-cycle-ii/"

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_node = ListNode(0, head)
        slow = dummy_node
        fast = dummy_node
        flag = False
        # check if there is a cycle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                flag = True
                break
        # find the node where the cycle begins
        if flag:
            fast = dummy_node
            while fast:
                fast = fast.next
                slow = slow.next
                if slow == fast:
                    return fast
                    #return slow
        
        return None
        
