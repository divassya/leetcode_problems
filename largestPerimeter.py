'''
Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106
'''
class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # condition to create a triangle a < (b + c). where  a >= b >= c
        nums = sorted(nums, reverse=True) # nums after sorting = [6, 3, 3, 2]
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] +nums[i+2]: # When i =1 => 3 < 3+2 (True)
                return nums[i]+nums[i+1] +nums[i+2] # 3 + 3 + 2 = 8
        return 0
