class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Initialize first pointer and last pointer
        firstP = 0
        lastP = len(s) - 1
        # Then I will use a for loop, and comparing the character, and only consider alphanumeric characters.
        while firstP < lastP:
            while firstP < lastP and not s[firstP].isalnum():
                firstP += 1 
            while firstP < lastP and not s[lastP].isalnum():
                lastP -= 1
            if s[firstP].lower() != s[lastP].lower():
                return False
            firstP += 1
            lastP -= 1
        return True


        