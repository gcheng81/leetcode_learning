"https://leetcode.com/problems/minimum-depth-of-binary-tree/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Soluton 1: BFS
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # BFS
        q = collections.deque()
        if root:
            q.append(root)
            depth = 1
        else:
            return 0
        
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            depth += 1
            
# Solution 2: DFS  
# Recursion
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        else:
            if not root.left and not root.right:
                return 1
        
            elif root.left and root.right:
                left_depth = self.minDepth(root.left)
                right_depth = self.minDepth(root.right)
                return 1 + min(left_depth, right_depth)
        
            elif root.left:
                left_depth = self.minDepth(root.left)
                return 1 + left_depth
        
            else:
                right_depth = self.minDepth(root.right)
                return 1 + right_depth
    
