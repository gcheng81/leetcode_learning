"https://leetcode.com/problems/maximum-depth-of-binary-tree/"

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q = collections.deque()
        count = 0
        #res = []
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
                #res.append(level)
                count += 1
        return count
        #return len(res)
        
