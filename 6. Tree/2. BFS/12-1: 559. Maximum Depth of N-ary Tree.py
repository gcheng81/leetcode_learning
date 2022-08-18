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
