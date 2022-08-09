"https://leetcode.com/problems/binary-tree-postorder-traversal/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive Traversal
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, right, mid
        res = []
        
        def traversal(node: TreeNode):
            if node == None:
                return
            traversal(node.left)
            traversal(node.right)
            res.append(node.val)
        
        traversal(root)
        return res
            

# Solution 2: Iterative Traversal
