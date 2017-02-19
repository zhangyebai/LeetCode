#!/usr/bin/env python
# _*_ coding:utf-8 _*_
"""
    @Author 张夜白 At LeetCode  self.__init__()是为了防止提示class method should be static method
    Write a function to find the longest common prefix string amongst an array of strings.
"""

class Solution(object):
    # 从索引的角度思考解题方法 挨个遍历对比每个字符串并取子串，提交的时候效率比下面的方法低
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.__init__()
        if not strs:
            return ""
        max_common_length = len(strs[0])
        length_of_list = len(strs)
        for i in range(0, length_of_list - 1):
            index = min(len(strs[i]), len(strs[i + 1]))
            temp_index = 0
            for n in range(0, index):
                if strs[i][n] != strs[i + 1][n]:
                    temp_index = n
                    break
                else:
                    temp_index = n + 1
            max_common_length = min(max_common_length, temp_index)
        return strs[0][0:max_common_length] if max_common_length > 0 else ""

    # 将list中第一个字符串作为公共最长前缀的串，然后遍历整个list中的字符串，挨个对比每个字符
    # 临界条件设置的很nice
    def longestCommonPrefixByCommonFator(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        self.__init__()
        if not strs:
            return ''
        for i in range(len(strs[0])):
            for data in strs:
                if len(data) <= i or data[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]

if __name__ == '__main__':
    print(Solution().longestCommonPrefixByCommonFator(["ccc", "cca", "cb"]))

