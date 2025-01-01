class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            diff = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] < diff:
                    l = mid + 1
                else:
                    r = mid - 1
        return []
            
                    



        # left = 0
        # right = len(numbers) - 1 
        # while left < right:
        #     currSum = numbers[left] + numbers[right]
        #     if currSum > target:
        #         right -= 1
        #     elif currSum < target:
        #         left += 1
        #     else:
        #         return [left + 1, right + 1]
        
            
        