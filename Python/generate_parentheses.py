#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution:
    def helper(self, l, r, item, res):
        print(item, l, r, sep="--")
        if r < l:
            return
        if l == 0 and r == 0:
            res.append(item)
        if l > 0:
            self.helper(l - 1, r, item + '(', res)
        if r > 0:
            self.helper(l, r - 1, item + ')', res)

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        res = []
        self.helper(n, n, '', res)
        return res


if __name__ == '__main__':
    print(Solution().generateParenthesis(2))