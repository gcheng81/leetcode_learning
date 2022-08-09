"https://leetcode.com/problems/binary-tree-preorder-traversal/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Recursive Traversal
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # mid, left, right
        res = []
        
        def traversal(node: TreeNode):
            if node == None:
                return 
            res.append(node.val)
            traversal(node.left)
            traversal(node.right)
        
        traversal(root)
        return res

# Solution 2: Iterative Traversal
# !Notice: The order of entering the stack
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # mid, left, right
        if root == None:
            return []
        
        res = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            # append mid
            res.append(cur_node.val)
            # push right
            if cur_node.right:
                stack.append(cur_node.right)
            # push left
            if cur_node.left:
                stack.append(cur_node.left)
        return res
