#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Title: Longest Substring Without Repeating Characters:
    Given a string, find the length of the longest substring without repeating characters.

    Examples:
        Given "abcabcbb", the answer is "abc", which the length is 3.
        Given "bbbbb", the answer is "b", with the length of 1.
        Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring,
        "pwke" is a subsequence and not a substring.
        Subscribe to see which companies asked this question
"""
import time


def fun_time(fn):
    def _wrapper(*args, **kwargs):
        start = time.clock()
        result = fn(*args, **kwargs)
        # print("%s cost %s second, result = %s " % (fn.__name__, time.clock() - start, result))
        # return result
        return "%s cost %s second, result = %s " % (fn.__name__, time.clock() - start, result)
    return _wrapper


class Solution(object):
    @fun_time
    def lengthOfLongestSubstring(self, s: str)->int:
        """
        :type s: str
        :rtype: int
        """
        self.__init__()
        data = str(s)
        length = len(data)
        bit_list = [0 * i for i in range(1, 256)]
        start, end, max_string_length = 0, 0, 0
        index = 1
        while index <= length:
            if bit_list[ord(data[index - 1])] > start:
                start = bit_list[ord(data[index - 1])]

            max_string_length = max(max_string_length, index - start)
            bit_list[ord(data[index - 1])] = index
            index += 1

        return max_string_length

    @fun_time
    def lengthOfLongestSubstring2(self, s: str)->int:

        self.__init__()
        data, loop, max_string_length = {}, 0, 0
        for i, char in enumerate(s):
            if char in data and data[char] >= loop:
                loop = data[char] + 1
            data[char] = i
            max_string_length = max(max_string_length, i - loop + 1)
            # step by step to find the longest substring
            # print(data, 'max_string_length' + str(max_string_length), 'loop' + str(loop), sep=' : ')
        # print(data)
        return max_string_length

if __name__ == '__main__':
    # print(Solution().lengthOfLongestSubstring('pwwkew'))
    # print(Solution().lengthOfLongestSubstring2('pwwkew'))

    solution = Solution()
    print(solution.lengthOfLongestSubstring('pwwkew'))
    print(solution.lengthOfLongestSubstring2('pwwkew'))
