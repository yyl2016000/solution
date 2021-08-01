# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> list: 
        if not root: return []
        stack = [root]
        res = []
        while(stack): 
            cur = stack.pop()
            if not cur: 
                res.append(stack.pop().val)
            else:  
                if cur.right: 
                    stack.append(cur.right)
                stack.append(cur)
                stack.append(None)
                if cur.left: 
                    stack.append(cur.left)
        return res  

# 递归版本略，解析见leetcode.145