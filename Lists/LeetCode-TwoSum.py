# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
#
# return [0, 1].

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False
        buffer = {}
        for i in range(len(nums)):
            if nums[i] in buffer:
                return [buffer[nums[i]],i]
            else:
                buffer[target-nums[i]]=i


nums = [2, 7, 11, 15]
target = 9
twoSum(nums,target)
