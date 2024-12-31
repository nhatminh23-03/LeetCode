class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict_nums = {}
        for i,v in enumerate(nums):
            dict_nums[v] = i
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in dict_nums and dict_nums[diff] != i:
                return [i, dict_nums[diff]]