# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = collections.deque([(root, 1)])
        while(queue): 
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left: 
                queue.append([node.left, depth + 1]) 
            if node.right: 
                queue.append([node.right, depth + 1])

# 广度优先搜索，第一个找到的必定是深度最小的叶子节点