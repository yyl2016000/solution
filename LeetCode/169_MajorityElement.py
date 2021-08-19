class Solution:
    def majorityElement(self, nums: list) -> int:
        mapper = {} 
        for i in nums: 
            if i in mapper: 
                mapper[i] += 1 
                if mapper[i] > len(nums) // 2: 
                    return i 
            else: 
                mapper[i] = 1 
        return nums[0] 

    def majorityElement_(self, nums: list) -> int:
        res = None
        counter = 0
        for i in nums: 
            if counter == 0: res = i 
            counter = counter + 1 if i == res else counter -1 
        return res 

# 方法一采用hash的方法，时间、空间复杂度为O(n), O(n).
# 方法二采用摩尔投票法，时间、空间复杂度为O(n), O(1).