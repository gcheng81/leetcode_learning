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

    
# Solution 3: 标记法 or 统一迭代法
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # mid, left, right
        res = []
        stack = []
        
        if root:
            stack.append(root)
        
        while stack:
            cur = stack.pop()
            if cur:
                if cur.right:
                    stack.append(cur.right)
                
                if cur.left:
                    stack.append(cur.left)
                
                stack.append(cur)
                stack.append(None)
            
            else:
                cur = stack.pop()
                res.append(cur.val)
        
        return res
                
