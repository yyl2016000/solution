# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int: 
        out_list = []

        def searchLeaves(root, out_list): 
            if not root.left: 
                out_list.append(root.val)
                return None
            searchLeaves(root.left, out_list) 
            searchLeaves(root.right, out_list)
            return None

        searchLeaves(root, out_list)
        out_list.sort()
        # print(out_list)
        for i in out_list: 
            if i != out_list[0]:
                return i
        return -1

class Solution_2:
    def find2ndMinValue(self, root): 
        if not root.left: 
            return -1 

        if root.left.val == root.right.val: 
            result_l = self.find2ndMinValue(root.left)
            result_r = self.find2ndMinValue(root.right)
            if result_l == -1 or result_r == -1:
                return max(result_l, result_r)
            else:
                return min(result_l, result_r)
        
        else:
            minTree, theValue = (root.left, root.right.val) if root.left.val < root.right.val else (root.right, root.left.val)

            result = self.find2ndMinValue(minTree)

            if result == -1: 
                return theValue
            else:
                if result == root.val or result >= theValue: 
                    return theValue
                else: 
                    return result


    def findSecondMinimumValue(self, root: TreeNode) -> int: 
        result = self.find2ndMinValue(root)
        if result == root.val: return -1
        return result

class Solution_best: 
    def findSecondMinimumValue(self, root: TreeNode) -> int: 
        if not root or not root.left: 
            return -1
        left = root.left.val if root.left.val != root.val else self.findSecondMinimumValue(root.left)
        right = root.right.val if root.right.val != root.val else self.findSecondMinimumValue(root.right)
        return min(left, right) if left != -1 and right != -1 else max(left, right)
