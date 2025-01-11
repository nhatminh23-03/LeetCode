class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charSet = set()
        res = 0 
        l = 0 
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 
            charSet.add(s[r])
            res = max(res, len(charSet))
        return res
            
        