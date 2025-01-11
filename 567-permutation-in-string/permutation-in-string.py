class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) > len(s2):
            return False
        countS1, countS2 = [0] * 26, [0] * 26
        for c in range(len(s1)):
            countS1[ord(s1[c]) - ord("a")] += 1 
            countS2[ord(s2[c]) - ord("a")] += 1 
        
        matches = 0
        for i in range(len(countS1)):
            matches += (1 if countS1[i] == countS2[i] else 0)
        
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True

            index = ord(s2[r]) - ord("a")
            countS2[index] += 1 
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] + 1 == countS2[index]:
                matches -= 1
            
            index = ord(s2[l]) - ord("a")
            countS2[index] -= 1 
            if countS1[index] == countS2[index]:
                matches += 1
            elif countS1[index] - 1 == countS2[index]:
                matches -= 1
            l += 1 
        return matches == 26
            
            
        