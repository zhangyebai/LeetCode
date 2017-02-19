#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = None
        if not digits:
            return []
        digit_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        for i in digits:
            if result is None:
                result = [y for y in digit_map[i]]
            else:
                result = [x + y for x in result for y in digit_map[i]]
        return result

if __name__ == '__main__':
    print(Solution().letterCombinations("2"))
