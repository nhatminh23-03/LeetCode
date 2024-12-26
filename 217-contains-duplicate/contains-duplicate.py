class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        set_nums = set()
        for i in nums:
            if i in set_nums:
                return True
            set_nums.add(i)
        return False
    
        