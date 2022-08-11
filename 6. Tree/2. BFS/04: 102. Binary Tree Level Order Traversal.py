"https://leetcode.com/problems/binary-tree-level-order-traversal/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: Iteration
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = collections.deque()
        if root:
            q.append(root)
        
        while q:
            q_len = len(q)
            level = []
            for _ in range(q_len): # len(q) will change, so we need q_len
                cur = q.popleft()
                if cur:
                    level.append(cur.val)
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
            
            if level:
                res.append(level)
        return res
      
 # Solution 2: Recursion
