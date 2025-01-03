class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 2 Pointer Technique
        res = 0
        l, r = 0, len(height) - 1 
        while l < r:
            rectangle = (r - l) * (min(height[l], height[r]))
            res = max(res, rectangle)
            if height[l] <= height[r]:
                l += 1
            else:
                r -= 1
        return res


        # Bruce Force 
        # res = 0
        # for i in range(len(height)):
        #     for j in range(1, len(height)):
        #         rectangle = (j - i) * (min(height[i], height[j]))
        #         res = max(res, rectangle)
        # return res
        