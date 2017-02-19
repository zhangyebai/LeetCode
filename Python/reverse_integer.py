#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Reverse digits of an integer.
    Example1: x = 123, return 321
    Example2: x = -123, return -321

    Have you thought about this?
    Here are some good questions to ask before coding.
    Bonus points for you if you have already thought through this!
    If the integer's last digit is 0, what should the output be?
    ie, cases such as 10, 100.
    Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer,
     then the reverse of 1000000003 overflows. How should you handle such cases?
    For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

    remember that, don't do it using convert int to string and reverse the string
    Note the second part,
"""


class Solution(object):
    def reverse(self, x: int)->int:
        """
        :type x: int
        :rtype: int
        """
        self.__init__()
        int_num = x if x >= 0 else 0 - x
        int_max = 0x7fffffff  # 2147483647
        int_min = -0x80000000  # -2147483648
        num_sign = True if x >= 0 else False
        reverse_x = 0
        while int_num != 0:
            reverse_x = reverse_x * 10 + int_num % 10
            int_num //= 10
            print("reverse_x = %d, int_num = %d" % (reverse_x, int_num))
        if not num_sign:
            reverse_x = 0 - reverse_x
        return 0 if reverse_x > int_max or reverse_x < int_min else reverse_x

if __name__ == '__main__':
    print(Solution().reverse(21474836472147483647))
