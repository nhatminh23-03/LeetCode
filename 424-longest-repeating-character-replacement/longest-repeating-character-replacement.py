class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        l = 0
        dict_s = {}
        for r in range(len(s)):
            dict_s[s[r]] = 1 + dict_s.get(s[r], 0)
            while (r - l + 1) - max(dict_s.values()) > k:
                dict_s[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

        