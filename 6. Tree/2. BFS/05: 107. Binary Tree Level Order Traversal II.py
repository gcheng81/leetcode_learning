"https://leetcode.com/problems/binary-tree-level-order-traversal-ii/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Interation
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            level = []
            for _ in range(size):
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
            if level:
                res.append(level)
        return res[::-1]
        
