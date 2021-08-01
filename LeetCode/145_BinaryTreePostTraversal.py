# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list:
        if not root: return []
        stack = [root]
        res = []
        while(stack): 
            cur = stack.pop()
            if not cur: 
                res.append(stack.pop().val)
            else:  
                stack.append(cur)
                stack.append(None)
                if cur.right: 
                    stack.append(cur.right)
                if cur.left: 
                    stack.append(cur.left)
        return res 

# 这是一种利用迭代而不是递归进行树的遍历通用的方法，对于前序、中序、后序遍历只需要更改加入空节点的位置即可。
# 在本方法中，会对树中的每个节点访问两次，第一次将其左右子节点加入到栈中，然后再次将其压入栈中，并在其上压
# 入一个空节点，这样，在第二次访问到该节点（即回溯）时可以知道该节点已经访问过一次，直接输出该节点值即可。