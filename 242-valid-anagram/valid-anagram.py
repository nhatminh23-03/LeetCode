class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
            
        dict_s = {}
        dict_t = {}
        for c in s:
            dict_s[c] = 1 + dict_s.get(c, 0)
        for c in t:
            dict_t[c] = 1 + dict_t.get(c, 0)
        return dict_s == dict_t
        
