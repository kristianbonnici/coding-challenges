"""
TASK: Given an integer array nums, find the contiguous subarray (containing at least one number)
      which has the largest sum and return its sum.

      A subarray is a contiguous part of an array.
"""
from numpy import cumsum, max


class Solution(object):
    def max_subarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum_list = []
        for i in range(0, len(nums)):
            sum_list.extend(cumsum(nums[i:]))
        return max(sum_list)
