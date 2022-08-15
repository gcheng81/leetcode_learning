"https://leetcode.com/problems/n-ary-tree-postorder-traversal/"

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Solution 1: Recursion
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # left, right, mid
        stack = []
        
        def dfs_post(node):
            if node==None:
                return
            for child in node.children:
                dfs_post(child)
            stack.append(node.val)
        
        dfs_post(root)
        return stack
    
 # Solution 2: Iteration
