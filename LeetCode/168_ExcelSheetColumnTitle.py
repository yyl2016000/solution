class Solution:
    def convertToTitle(self, columnNumber: int) -> str: 
        res = ''
        while(columnNumber): 
            columnNumber -= 1 
            res = chr(columnNumber % 26 + 65) + res 
            columnNumber = columnNumber // 26
        return res

# 乍一看好像是26进制，但是该表示方法中没有0，每一位应该看作从上一位中借了1，因此从1而不是0开始（即从'A'开始）
# 其实还是没完全懂......先记住吧