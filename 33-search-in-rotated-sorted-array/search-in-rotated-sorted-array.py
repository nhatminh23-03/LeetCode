class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l, r = 0, len(nums) - 1 
        while l <= r:
            mid = (l + r) // 2 
            # Determine if mid is in what sorted portion
            # On the second sorted portion
            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[l]: 
                if target < nums[l] or nums[mid] < target:
                    l = mid + 1
                else:
                    r = mid - 1 
            else:
                if nums[mid] > target or nums[r] < target:
                    r = mid - 1 
                else:
                    l = mid + 1
        return -1 
        