"https://leetcode.com/problems/populating-next-right-pointers-in-each-node/"

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# Solution 1: DFS--Recursion
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        def connect_two_nodes(node1, node2):
            if node1 is None or node2 is None:
                return
            node1.next = node2
            # same node
            connect_two_nodes(node1.left, node1.right)
            connect_two_nodes(node2.left, node2.right)
            # different node
            connect_two_nodes(node1.right, node2.left)
        
        if root is None:
            return
        connect_two_nodes(root.left, root.right)
        return root
        
