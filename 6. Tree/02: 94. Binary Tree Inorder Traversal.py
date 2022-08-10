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
        
# Solution 2: Iterative Traversal
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, mid, right
        stack = []
        res = []
        cur = root
        
        while cur or stack:
            if cur: # 先迭代访问最底层的左子树结点
                stack.append(cur)
                cur = cur.left
            else:  # 到达最左结点后处理栈顶结点
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right # 取栈顶元素右结点
        return res
  
########## Or:
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, mid, right
        stack = []
        res = []
        cur = root
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res    

 
# Solution 3: 标记法 or 统一迭代法
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # left, mid, right
        res = []
        stack = []
        
        if root:
            stack.append(root)
        
        while stack:
            cur = stack.pop()
            if cur:
                if cur.right:
                    stack.append(cur.right)
                
                stack.append(cur)
                stack.append(None) #中节点访问过，但是还没有处理，加入空节点做为标记
                
                if cur.left:
                    stack.append(cur.left)
            
            else:#只有遇到空节点的时候，才将下一个节点放进结果集
                cur = stack.pop()
                res.append(cur.val)
        
        return res
