"https://leetcode.com/problems/balanced-binary-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.get_height(root)<0:
            return False
        return True
        
    def get_height(self, root):
        if root is None:
            return 0
        left_height = self.get_height(root.left)
        right_height = self.get_height(root.right)
        # not balanced
        if left_height<0 or right_height<0 or abs(left_height-right_height)>1:
            return -1
        # balanced
        return max(left_height, right_height)+1
    
        
