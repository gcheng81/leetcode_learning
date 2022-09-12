"https://leetcode.com/problems/binary-tree-level-order-traversal/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1: BFS: Iteration
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        q = collections.deque()
        q.append(root)
        
        while q:
            level = []
            size = len(q)
            for _ in range(size):# len(q) will change, so we need size
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
