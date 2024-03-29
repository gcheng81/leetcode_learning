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
        res = []
        def traverse(node):
            if node is None:
                return
            for child in node.children:
                traverse(child)
            res.append(node.val)
        traverse(root)
        return res
    
 # Solution 2: Iteration
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        # left, right, mid
        stack = []
        res = []
        
        if root:
            stack.append(root)
        
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.extend(cur.children)
                
        return res[::-1]
