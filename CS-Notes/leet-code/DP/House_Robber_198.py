'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

def MySolution(nums: list) -> int: 
    n = len(nums)
    if n < 3: 
        return max(nums)
    dp = [[nums[0], 0], [nums[1], nums[0]]]
    for i in range(2, n):
        dp.append([0, 0])
        dp[i][0] = nums[i] + max(dp[i-2])
        dp[i][1] = max(dp[i-1])
    return max(dp[-1])

def solution(nums: list) -> int:
    pre1, pre2 = 0, 0 
    for i in range(len(nums)): 
        cur = max(pre1+nums[i], pre2)
        pre1, pre2 = pre2, cur
    return pre2

def main(): 
    # print(MySolution(list(map(int, input().split()))))
    print(solution(list(map(int, input().split()))))

if __name__ == '__main__': 
    main()