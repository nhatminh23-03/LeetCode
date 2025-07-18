# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # if not root:
        #     return 0
        
        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # DFS 
        if not root:
            return 0

        stack = [[root, 1]]

        level = 0

        while stack:
            node, depth = stack.pop()

            if node:
                level = max(level, depth)
                stack.append([node.right, depth + 1])
                stack.append([node.left, depth + 1])
        
        return level



        
        