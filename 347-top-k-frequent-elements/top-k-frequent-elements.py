class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_nums  = {}
        freq = [[] for i in range(len(nums) + 1)]
        for i in nums:
            dict_nums[i] = 1 + dict_nums.get(i, 0)
        for num, count in dict_nums.items():
            freq[count].append(num)
        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)
            if len(result) == k:
                return result
        