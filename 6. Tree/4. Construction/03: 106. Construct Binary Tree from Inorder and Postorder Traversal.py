"https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder)==0 or len(postorder)==0:
            return None
        
        root = TreeNode(postorder[-1])
        inorder_root_index = inorder.index(postorder[-1])
        root.left = self.buildTree(inorder[:inorder_root_index], postorder[:inorder_root_index])
        root.right = self.buildTree(inorder[inorder_root_index+1:], postorder[inorder_root_index:-1])
        return root
