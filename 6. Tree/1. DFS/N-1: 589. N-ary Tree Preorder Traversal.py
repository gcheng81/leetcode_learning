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
        # mid, left, right
        stack = []
        def dfs_pre(node):
            if node==None:
                return
            stack.append(node.val)
            for child in node.children:
                dfs_pre(child)
        
        dfs_pre(root)
        return stack

      
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

        
      
