#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return False
        key_map = {'[': ']', '{': '}', '(': ')'}
        stack = []
        for i in s:
            if i in key_map.keys():
                stack.append(i)
            elif i in key_map.values():
                if not stack:
                    return False
                elif i != key_map[stack[-1]]:
                    return False
                else:
                    stack.pop()
            else:
                return False
        return not stack


if __name__ == '__main__':
    print(Solution().isValid('()'))
