"https://leetcode.com/problems/n-ary-tree-level-order-traversal/"

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
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
                if cur.children:
                    q.extend(cur.children) # type(children) = list 
            if level:
                res.append(level)
        return res
