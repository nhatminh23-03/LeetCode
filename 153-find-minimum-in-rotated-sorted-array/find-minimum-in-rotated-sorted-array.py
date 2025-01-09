class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = nums[0]
        l, r = 0, len(nums) - 1 
        while l <= r:
            if nums[l] < nums[r]:
                min_val = min(min_val, nums[l])
                break

            mid = (l + r) // 2
            min_val = min(min_val, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1 
                
        return min_val
