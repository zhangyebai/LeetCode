#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.__init__()
        result = []
        nums.sort()
        length = len(nums)
        for i in range(length - 3):
            if i and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, length - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                sum_ = target - nums[i] - nums[j]
                left, right = j + 1, length - 1
                while left < right:
                    if nums[left] + nums[right] == sum_:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        right -= 1
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif nums[left] + nums[right] > sum_:
                        right -= 1
                    else:
                        left += 1
        return result