class Solution:
    def titleToNumber(self, columnTitle: str) -> int: 
        res = 0 
        for i in columnTitle: 
            res *= 26
            res += ord(i) - 64
        return res 

'''
    26进制转10进制，最直观的方法是从低位到高位依次转化，此解法为利用公因式提取从高位开始转化
'''