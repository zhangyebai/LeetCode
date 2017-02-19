#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Title: Two Sum
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution.
    Example:
        Given nums = [2, 7, 11, 15], target = 9,
        Because nums[0] + nums[1] = 2 + 7 = 9,
        return [0, 1].

    UPDATE (2016/2/13):
    The return format had been changed to zero-based indices. Please read the above updated description carefully.
    Subscribe to see which companies asked this question
"""


class TwoNum(object):
    @staticmethod
    def two_num(nums, target)->object:
        nums_dict = {}
        for loop, value in enumerate(nums):
            if nums_dict.__contains__(target - value):
                return [nums_dict[target - value], loop]
            else:
                nums_dict[value] = loop

if __name__ == '__main__':
    num_list = [2, 7, 11, 15]
    target_num = 22
    result = TwoNum.two_num(num_list, target_num)
    try:
        for index in result:
            print('->'.join([str(index), str(num_list[index])]))
    except TypeError:
        print('no target to find')
