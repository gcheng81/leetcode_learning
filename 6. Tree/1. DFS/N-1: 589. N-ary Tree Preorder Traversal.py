"https://leetcode.com/problems/n-ary-tree-preorder-traversal/"

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# Solution 1: Recursion
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def traverse(node):
            if node is None:
                return
            res.append(node.val)
            for child in node.children:
                traverse(child)
        traverse(root)
        return res

      
# Solution 2: Iteration
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # mid, left, right
        stack = []
        res = []
        if root:
            stack.append(root)
            
        while stack:
            cur = stack.pop()
            if cur:
                res.append(cur.val)
                stack.extend(cur.children[::-1])
            
        return res

        
      
