from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # use defaultdict to avoid edge case 
        dict_str = defaultdict(list)
        
        for s in strs:
            count  = [0] * 26 # a-z
            for c in s:
                count[ord(c) - ord("a")] += 1 
            dict_str[tuple(count)].append(s)

        return list(dict_str.values())