# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums) -> TreeNode:
        
        if not nums: return None
        if len(nums) == 1: return TreeNode(nums[0])

        mid = len(nums) // 2
        root = TreeNode(nums[mid]) 
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root

    # 这种解法会重复传递nums，空间复杂度上升，后续还是要改成传数组下标的形式