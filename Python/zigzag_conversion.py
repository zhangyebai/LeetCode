#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Title: ZigZag Conversion
    The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
     (you may want to display this pattern in a fixed font for better legibility)
        P   A   H   N
        A P L S I I G
        Y   I   R

    And then read line by line: "PAHNAPLSIIGYIR"
    Write the code that will take a string and make this conversion given a number of rows:
    string convert(string text, int nRows);
    convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
"""


class Solution(object):
    def convert(self, s: str, numRows: int)-> str:
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        self.__init__()
        length = len(s)
        data = []
        if length <= 0 or numRows <= 1:
            return s
        zigzag_carry = 2 * numRows - 2
        for i in range(numRows):
            for j in range(i, length, zigzag_carry):
                data.append(s[j])
                if i != 0 and i != numRows - 1 and zigzag_carry + j - 2 * i < length:
                    data.append(s[zigzag_carry + j - 2 * i])

        return ''.join(data)

    def print_zigzag_string(self, s: str, numRows: int)->str:
        self.__init__()
        length = len(s)
        result = []
        if length <= 0 or numRows <= 1:
            return s
        zigzag_carry = 2 * numRows - 2
        zig_space = numRows - 2
        for i in range(numRows):
            for j in range(i, length, zigzag_carry):
                result.append(s[j])
                if i != 0 and i != numRows - 1 and zigzag_carry + j - 2 * i < length:
                    for r in range(zig_space - i):
                        result.append(' ')
                    result.append(s[zigzag_carry + j - 2 * i])
                    for n in range(i - 1):
                        result.append(' ')
                else:
                    for m in range(zig_space):
                        result.append(' ')
            result.append('\r\n')
        return ''.join(result)

if __name__ == '__main__':
    print(Solution().convert('PAYPALISHIRING', 3))
    print(Solution().print_zigzag_string('abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', 20))
