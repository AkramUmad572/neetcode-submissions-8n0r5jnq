"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        
        def dfs(node):
            if not node:
                return None
            if node in cloned:
                return cloned[node]
            new_clone = Node(node.val)
            cloned[node] = new_clone
            
            for node in node.neighbors:
                new_nei = dfs(node)
                new_clone.neighbors.append(new_nei)
            
            return new_clone
            

        return dfs(node)




