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
        res = []
        
        # mid left right
        def traverse(node):
            if node is None:
                return
            
            # 如果单独抽出一个二叉树节点，它需要做什么事情？Action: add value to res array
            # 需要在什么时候（前/中/后序位置）做？前
            res.append(node.val)
            traverse(node.left)
            traverse(node.right)
        
        traverse(root)
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
                
