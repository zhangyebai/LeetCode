#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

    Example:
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.

    Example:
        Input: "cbbd"
        Output: "bb"
"""


class Solution(object):
    # Manacher算法
    def longestPalindrome(self, s: str)->str:
        """
        :type s: str
        :rtype: str
        """
        self.__init__()
        temp_str = ''.join(['^#', '#'.join(s), '#$'])
        length = len(temp_str)

        loop_palindrome_center, right_palindrome_index = 0, 0
        carry_list = [0] * length
        for i in range(1, length - 1):
            '''
            print("index = %d, carry_list[%d] = %d, loop_palindrome_center = %d, right_palindrome_index = %d" %
                  (i, i, carry_list[i], loop_palindrome_center, right_palindrome_index),
                  end='\r\n***************************\r\n')
            '''
            # index_left-> Loop到当前索引i时围绕中心点loop_palindrome_center在左边的对称点索引
            index_left = loop_palindrome_center - (i - loop_palindrome_center)
            # 判断当前索引i是否在以loop_palindrome_center为中心的右探right_palindrome_index范围内
            carry_list[i] = min(right_palindrome_index - i, carry_list[index_left]) if right_palindrome_index > i else 0
            while temp_str[i + 1 + carry_list[i]] == temp_str[i - 1 - carry_list[i]]:
                carry_list[i] += 1

            if i + carry_list[i] > right_palindrome_index:
                loop_palindrome_center = i
                right_palindrome_index = i + carry_list[i]
            '''
            print("index = %d, carry_list[%d] = %d, loop_palindrome_center = %d, right_palindrome_index = %d" %
                  (i, i, carry_list[i], loop_palindrome_center, right_palindrome_index), end='\r\n\r\n')
            '''
        '''
        print(list(temp_str))
        print([str(i) for i in carry_list])
        '''
        max_length, center_index = 0, 0
        for index in range(length):
            if max_length < carry_list[index]:
                max_length = carry_list[index]
                center_index = index
        return s[(center_index - 1 - max_length) // 2: (center_index - 1 - max_length) // 2 + max_length]

    # Dynamic Programming 动态规划枚举
    def longestPalindromeDynamicProgramming(self, s: str) -> str:
        length = len(s)
        left, right, max_length = 0, 0, 1
        dp_table = [[0 * j for j in range(length)] for i in range(length) if i < length]
        for i in range(length):
            dp_table[i][i] = 1
            for j in range(i):
                # print(i, j)
                dp_table[j][i] = 1 if s[i] == s[j] and (i - j < 2 or dp_table[j + 1][i - 1] == 1) else 0
                '''
                for index, data_list in enumerate(dp_table):
                    print(data_list)
                print()
                '''
                if dp_table[j][i] == 1 and max_length < i - j + 1:
                    max_length = i - j + 1
                    left, right = j, i + 1
                    '''
                    print(left, right)
        for index, data_list in enumerate(dp_table):
            print(data_list)
            '''
        return s[left: right]

    # time complexity O(n ^ 3)
    # auxiliary complexity O(1)
    # 暴力枚举
    def longestPalindromeBruteForce(self, s: str)->str:
        """
        :type s: str
        :rtype: str
        """
        start, end = 0, 0
        self.__init__()
        for i in range(len(s) + 1):
            for j in range(i + 1, len(s) + 1):
                # print(i, j, end='->')
                # print(s[i:j])
                if self.string_is_palindrome(s[i:j]):
                    # result.append([i, j])
                    if end - start < j - i:
                        start, end = i, j

        return s[start:end]

    # 判断字符串是否是回文字符串，不考虑子串的情况
    # 暴力枚举算法的辅助函数
    def string_is_palindrome(self, s: str)->bool:
        """
        :type s: str
        :rtype: bool
        """
        self.__init__()
        length = len(s)
        if length <= 1:
            return False

        carry = length % 2
        for i in range(length):
            if i == length / 2 + carry:
                return True

            if s[i] != s[length - i - 1]:
                return False

        return True

if __name__ == '__main__':
    print(Solution().longestPalindrome('bananas'))
    # print(Solution().string_is_palindrome('ab'))
