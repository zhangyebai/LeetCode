#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Implement regular expression matching with support for '.' and '*'.
    '.' Matches any single character.
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    The function prototype should be:
    bool isMatch(const char *s, const char *p)

    Some examples:
    isMatch("aa","a") → false
    isMatch("aa","aa") → true
    isMatch("aaa","aa") → false
    isMatch("aa", "a*") → true
    isMatch("aa", ".*") → true
    isMatch("ab", ".*") → true
    isMatch("aab", "c*a*b") → true
"""

import re


class Solution(object):
    # Dynamic Programming
    def isMatch(self, s: str, p: str):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        len_s, len_p = len(s), len(p)
        data_base = [[i * 0 for i in range(len_p + 1)] for j in range(len_s + 1)]
        data_base[0][0] = 1
        for i in range(1, len_p + 1):
            if p[i - 1] == '*':
                data_base[0][i] = data_base[0][i - 2]
        print('\r\n'.join([str(elem) for elem in data_base]))
        print()
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if p[j - 1] == '*':
                    data_base[i][j] = data_base[i][j - 2]
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        data_base[i][j] |= data_base[i - 1][j]
                    # if p[i - 2] == '.':
                    #    data_base[i]
                else:
                    if s[i - 1] == p[j - 1] or p[j - 1] == '.':
                        data_base[i][j] = data_base[i - 1][j - 1]
        print('\r\n'.join([str(elem) for elem in data_base]))
        return data_base[len_s][len_p] == 1


    # Recursive
    # 提交在leetcode跑到匹配"aaaaaaaaaaaaab", "a*a*a*a*a*a*a*a*a*a*c"的时候超时
    # 目前没想出来如何让其不超时
    def isMatch_Recursive(self, s: str, p: str)->bool:
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        if p == '':
            return s == ''
        len_p = len(p)
        if s == '':
            # some extremity example(just like: a*.b*) also didn't match this empty string
            # because the src is empty
            # only the char on odd position in the string is '*',it matches the empty string
            if len_p % 2 == 1:
                return False
            else:
                for i in range(1, len_p, 2):
                    if p[i] != '*':
                        return False

                return True

        if len_p > 1 and p[1] == '*':
            # return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            if p[0] == '.' or p[0] == s[0]:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
            else:
                return self.isMatch(s, p[2:])
        elif p[0] == '.':
            return self.isMatch(s[1:], p[1:])
        elif p[0] == s[0]:
            return self.isMatch(s[1:], p[1:])
        else:
            return False


if __name__ == '__main__':
    print(Solution().isMatch("aa", "a*"))
    print(re.match("^a*a*a*a*a*a*a*a*a*a*c$", "aaaaaaaaaaaaab") is not None)
    pattern = re.compile('(^w+)\.python\.org')
    print(pattern.match("www.python.org") is not None)
