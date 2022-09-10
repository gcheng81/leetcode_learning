"https://leetcode.com/problems/invert-binary-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: DFS
# Recursion
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return
        # 如果单独抽出一个二叉树节点，它需要做什么事情？Action: switch its left and right
        # 需要在什么时候（前/中/后序位置）做？前/后
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

    
# Solution 2: BFS
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = collections.deque()
        
        if root:
            q.append(root)
        
        while q:
            cur = q.popleft()
            cur.left, cur.right = cur.right, cur.left
            
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        return root
