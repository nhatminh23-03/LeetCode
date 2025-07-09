class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dictS = {}
        l = 0
        res = 0 
        for r in range(len(s)):
            dictS[s[r]] = 1 + dictS.get(s[r], 0)
            while (r - l + 1) - max(dictS.values()) > k:
                dictS[s[l]] -= 1
                l = l + 1
            res = max(res, (r - l + 1))
        return res
        