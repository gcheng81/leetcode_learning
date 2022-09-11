"https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 如何按题目要求把一棵树拉平成一条链表？
# 1、将root的左子树和右子树拉平。
# 2、将root的右子树接到左子树下方，然后将整个左子树作为右子树。
# Solution 1: DFS Recursion
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # flatten tree and return list tail
        def flatten_tree(node):
            if node is None:
                return None
            
            if not node.left and not node.right:
                return node
            # 1. flatten
            left_tail = flatten_tree(node.left)
            right_tail = flatten_tree(node.right)
            # 2. connect
            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None
            
            return right_tail if right_tail else left_tail
        
        flatten_tree(root)
