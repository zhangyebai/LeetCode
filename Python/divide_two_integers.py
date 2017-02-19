#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        if divisor == 0:
            return INT_MAX
        result_negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a, b = abs(dividend), abs(divisor)
        result, shift = 0, 31
        while shift >= 0:
            if a >= b << shift:
                a -= b << shift
                result += 1 << shift
            shift -= 1
        if result_negative:
            result = - result
        if result > INT_MAX or result < (-INT_MAX - 1):
            return INT_MAX
        return result

    # not ac , because TLE了，必须得用位运算
    def divideMySelf(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        INT_MAX = 2 ** 31 - 1
        if divisor == 0:
            return INT_MAX
        result_negative = (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0)
        a, b = abs(dividend), abs(divisor)
        result = 0
        while a - b >= 0:
            result += 1
            a -= b
        if result_negative:
            result = - result
        if result > INT_MAX or result < (-INT_MAX - 1):
            return INT_MAX
        return result

if __name__ == '__main__':
    print(Solution().divide(1, 1))