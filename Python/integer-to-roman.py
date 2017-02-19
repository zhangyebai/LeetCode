#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    integer-to-roman: Given an integer, convert it to a roman numeral.
    Input is guaranteed to be within the range from 1 to 3999.
"""

'''
    罗马数字共有7个，即I(1)，V(5)，X(10)，L(50)，C(100)，D(500)，M(1000)
'''


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        self.__init__()
        if num < 1 or num > 3999:
            return None
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return M[num // 1000] + C[(num % 1000) // 100] + X[(num % 100) // 10] + I[num % 10]
if __name__ == '__main__':
    print(Solution().intToRoman(223))
