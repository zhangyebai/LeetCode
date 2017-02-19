#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Title: Palindrome Number
    Determine whether an integer is a palindrome.
    Do this without extra space.(Note this, no extra space)

    Could negative integers be palindromes? (ie, -1)
    If you are thinking of converting the integer to string, note the restriction of using extra space.
    You could also try reversing an integer. However, if you have solved the problem "Reverse Integer",
    you know that the reversed integer might overflow. How would you handle such case?
    There is a more generic way of solving this problem.
    Subscribe to see which companies asked this question
"""


class Solution(object):
    def isPalindrome(self, x: int)->bool:
        """
        :type x: int
        :rtype: bool
        """
        self.__init__()
        if x < 0:
            return False
        elif x == 0:
            return True

        base = 1
        while x // base >= 10:
            base *= 10

        while x != 0 and base != 0:
            if x // base != x % 10:
                return False

            # 每次loop将num去头去
            x = (x % base) // 10
            # 每次loop将base地板除100，因为num每次去掉头尾是2位
            base //= 10 ** 2
        return True


if __name__ == '__main__':
    c = 1214151531
    print(Solution().isPalindrome(1214151531))
