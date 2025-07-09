class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        countS1 = {}
        window = {}

        for i in range(n):
            countS1[s1[i]] = 1 + countS1.get(s1[i], 0)
            window[s2[i]] = 1 + window.get(s2[i], 0)

        if countS1 == window:
            return True
        
        for i in range(n, m):
            window[s2[i - n]] -= 1
            if window[s2[i-n]] == 0:
                del window[s2[i-n]]
            window[s2[i]] = 1 + window.get(s2[i], 0)

            if countS1 == window:
                return True 
        return False
        
        


        