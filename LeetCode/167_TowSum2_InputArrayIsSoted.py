class Solution:
    def twoSum(self, numbers: list, target: int) -> list:
        pre, post = 0, len(numbers) - 1
        while(pre < post): 
            sum_ = numbers[pre] + numbers[post] 
            if sum_ == target:  return [pre + 1, post + 1]
            if sum_ < target: 
                pre += 1
            else: 
                post -= 1   
        return [-1, -1]

# 本题使用了双指针解法，还可以使用哈希表求解，但空间复杂度会提升至O(n)