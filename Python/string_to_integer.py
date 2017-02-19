#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Title: String to Integer (atoi)
    Implement atoi to convert a string to an integer.
    Hint: Carefully consider all possible input cases. If you want a challenge,
    please do not see below and ask yourself what are the possible input cases.
    Notes: It is intended for this problem to be specified vaguely (ie, no given input specs).
    You are responsible to gather all the input requirements up front.
"""


class Solution(object):
        # the parameter given by leetcode is bull shit
    def myAtoi(self, str: str)-> int:
        """
        :type str: str
        :rtype: int
        """
        '''
        length = len(str)
        if length <= 1:
            return
        num_sign = True if
        '''
        str_num = str.strip()
        if not str_num:
            return 0
        int_max = 0x7fffffff  # 2147483647
        int_min = -0x80000000  # -2147483648
        num_sign = True  # if str_num[0] != '-' else False
        num_loop = False
        result = 0
        illegal_input = False
        length = len(str_num)
        for i in range(length):
            if str_num[i].isdigit():
                result = result * 10 + int(str_num[i])
                num_loop = True
            else:
                if num_loop:
                    # illegal_input = True
                    break
                else:
                    if str_num[i] == '-' and str_num[i] == '+':
                        illegal_input = True
                        break
                    else:
                        try:
                            if not str_num[i + 1].isdigit():
                                illegal_input = True
                                break
                            else:
                                if str_num[i] == '-':
                                    num_sign = False
                        except IndexError:
                            pass

                '''
                if not num_loop:
                    result = 0
                    try:
                        # 此处我保留异议，leetcode认为+-123为非法输入，但是我认为数字符号应该已接近数字的那个为准
                        # 为了通过test，做出以下修改

                        #if str_num[i] == '-' and str_num[i + 1].isdigit() and \
                        #        (str_num[i - 1] != '-' and str_num[i - 1] != '+'):
                        #    num_sign = False

                        if (str_num[i] == '-' or str_num[i] == '+') and \
                                ((str_num[i - 1] == '-' or str_num[i - 1] == '+')
                                 or (str_num[i + 1] == '-' or str_num[i + 1] == '+')):
                            illegal_input = True
                            break
                        if (str_num[i] == '-' or str_num[i] == '+') and  not str_num[i + 1].isdigit():
                            illegal_input = True
                            break
                        if str_num[i] == '-' and str_num[i + 1].isdigit() and \
                                (str_num[i - 1] != '-' and str_num[i - 1] != '+'):
                            num_sign = False
                    except IndexError:
                        pass
                else:
                    break
                '''
        if not num_sign:
            result = -result

        if illegal_input:
            result = 0
        if result > int_max:
            result = int_max
        elif result < int_min:
            result = int_min

        return result


if __name__ == '__main__':
    print(Solution().myAtoi("+1"))
