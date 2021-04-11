'''
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

'''

def MySolution(n: int) -> int: 
    dp = [1, 2]
    for i in range(2, n): 
        dp.append(dp[i-1] + dp[i-2])
    return dp[n-1]

def solution(n: int) -> int: 
    if n <= 2: 
        return n 
    pre1, pre2 = 1, 2
    for _ in range(2, n): 
        cur = pre1 + pre2 
        pre1, pre2 = pre2, cur
    return pre2

def main(): 
    # print(MySolution(int(input("输入一个正整数代表楼顶阶数:"))))
    print(solution(int(input("输入一个正整数代表楼顶阶数:"))))

if __name__ == '__main__':
    main()

'''
dp[i] 表示走到第 i 个楼梯的方法数目。
第 i 个楼梯可以从第 i-1 和 i-2 个楼梯再走一步到达，走到第 i 个楼梯的方法数为走到第 i-1 和第 i-2 个楼梯的方法数之和。
考虑到 dp[i] 只与 dp[i - 1] 和 dp[i - 2] 有关，因此可以只用两个变量来存储 dp[i - 1] 和 dp[i - 2]，使得原来的 O(N) 空间复杂度优化为 O(1) 复杂度。
'''