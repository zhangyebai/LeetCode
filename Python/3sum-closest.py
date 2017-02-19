#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < 0:
            target = -target
        nums.sort()
        length = len(nums)
        result = None
        if length <= 3:
            return sum(nums)
        for i in range(0, length - 1):
            left, right = i + 1, length - 1
            while left < right:
                sum_three_nums = nums[i] + nums[left] + nums[right]
                if result is None or abs(result - target) > abs(sum_three_nums - target):
                    result = sum_three_nums
                if sum_three_nums <= target:
                    left += 1
                else:
                    right -= 1
        return result


if __name__ == '__main__':
    print(Solution().threeSumClosest([1, 1, 1, 0], 100))
