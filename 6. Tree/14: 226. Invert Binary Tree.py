"https://leetcode.com/problems/invert-binary-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: BFS
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
