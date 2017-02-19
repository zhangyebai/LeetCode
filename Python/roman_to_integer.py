#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        length = len(s)
        for i in range(0, length - 1):
            if roman_map[s[i]] < roman_map[s[i + 1]]:
                result -= roman_map[s[i]]
            else:
                result += roman_map[s[i]]
        return result + roman_map[s[-1]]

if __name__ == '__main__':
    print(Solution().romanToInt("DCXXI"))
