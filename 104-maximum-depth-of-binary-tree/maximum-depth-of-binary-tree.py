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

            # BFS traversal 

            # if not root:
            #     return 0
            
            # level = 0
            # queue = deque([root])

            # while queue:
            #     for i in range(len(queue)):
            #         node = queue.popleft()
            #         if node.left:
            #             queue.append(node.left)
            #         if node.right:
            #             queue.append(node.right)
            #     level += 1 
                
            # return level

            # DFS Traversal

            if not root:
                return 0
            
            stack = [[root, 1]]
            level = 1 

            while stack:
                node, depth = stack.pop()

                if node:
                    level = max(level, depth)
                    stack.append([node.left, 1 + depth])
                    stack.append([node.right, 1 + depth])
            return level
        