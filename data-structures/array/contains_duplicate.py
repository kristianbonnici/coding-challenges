"""
TASK: Given an integer array nums, return true if any value appears at least twice in the array,
      and return false if every element is distinct.

EXAMPLES:
    Example 1:
        Input: nums = [1,2,3,1]
        Output: true
    Example 2:
        Input: nums = [1,2,3,4]
        Output: false

DIFFICULTY: Easy

(leetCode) Submission 09/24/2021 16:09
    Runtime: 96 ms (faster than 82.79% of Python submissions)
    Memory Usage: 19.1 MB (less than 56.26% of Python submissions)
"""


class Solution(object):
    def contains_duplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == len(set(nums)):
            return False
        else:
            return True
