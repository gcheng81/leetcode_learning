"https://leetcode.com/problems/maximum-depth-of-n-ary-tree/"

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# Solution 1: BFS
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        q = collections.deque()
        count = 0
        level = []
        if root:
            q.append(root)
        
        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur:
                    level.append(cur)
                for child in cur.children:
                    if child:
                        q.append(child)
            if level:
                count += 1
        return count

    
 # Solution 2: DFS-Recursion
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        if root.children == []:
            return 1
        
        depths = [self.maxDepth(child) for child in root.children]
        return 1 + max(depths)
        
           
