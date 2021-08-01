# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list:

        def helper(root, out_list): 
            if not root: return None
            out_list.append(root.val)
            helper(root.left, out_list)
            helper(root.right, out_list)
        
        out_list = []
        helper(root, out_list)
        return out_list

    def preorderTraversal_iteration(self, root: TreeNode) -> list: 
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
                if cur.left: 
                    stack.append(cur.left)
                stack.append(cur)
                stack.append(None)
        return res 
        
# 还有一种只需要O(1)空间复杂度的前序遍历方法——Morris遍历，有兴趣可以去学习
# 迭代法解析见leetcode.145