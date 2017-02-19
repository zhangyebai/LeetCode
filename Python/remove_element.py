#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        length = len(nums)
        index = 0
        for i in range(length):
            if val != nums[i]:
                nums[index] = nums[i]
                index += 1
        return index
