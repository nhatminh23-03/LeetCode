class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # create a dictionary
        dict_nums = {}
        # Use enumerate method to add to the dictionary
        for i, num in enumerate(nums):
            dict_nums[num] = i
        # Use for loop to check for the subtraction 
        for i, num in enumerate(nums):
            diff = target - num
            if diff in dict_nums and dict_nums[diff] != i:
                return [i, dict_nums[diff]]
        
        