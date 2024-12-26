class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Edge Case 
        if len(s) != len(t):
            return False
        
        # Using dictionary
        dict_s = {}
        dict_t = {}
        
        # Then I will use a for loop to loop through everycharacter in s and add that to the dictionaty and add up 1
        for i in range(len(s)):
            dict_s[s[i]] = 1 + dict_s.get(s[i], 0)
            dict_t[t[i]] = 1 + dict_t.get(t[i], 0)
        return dict_s == dict_t
            
        