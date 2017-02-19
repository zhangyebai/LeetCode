#pragma once

#include <vector>
#include <map>

class Solution {
public:
	std::vector<int> twoSum(std::vector<int>& nums, int target) {
		std::vector<int> result;
		std::map<int, int> loop;
		for (std::size_t index = 0; index < nums.size(); ++index)
		{
			if (loop.find(target - nums.at(index)) != loop.cend())
			{
				result.push_back(loop.at(target - nums.at(index)));
				result.push_back(index);
			}
			else
			{
				loop.insert(std::map<int, int>::value_type(nums.at(index), index));
			}
		}
		return result;
	}
};