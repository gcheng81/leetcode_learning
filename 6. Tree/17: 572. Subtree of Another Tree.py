"https://leetcode.com/problems/subtree-of-another-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursion
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.isSameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def isSameTree(self, s, t):
        if s is None and t is None:
            return True
        if s is None or t is None or s.val!=t.val:
            return False
        
        return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        
