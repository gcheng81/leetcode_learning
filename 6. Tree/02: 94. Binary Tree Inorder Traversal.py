"https://leetcode.com/problems/binary-tree-inorder-traversal/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, mid, right
        res = []
        
        def traversal(node: TreeNode):
            if node==None:
                return
            traversal(node.left)
            res.append(node.val)
            traversal(node.right)
        
        traversal(root)
        return res
        
