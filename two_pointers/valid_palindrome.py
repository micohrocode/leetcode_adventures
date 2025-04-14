class Solution(object):
    def isPalindrome(self, s):
        # format string as needed
        s = ''.join([i for i in s if i.isalnum()]).lower()

        # two pointers
        left = 0
        right = len(s)-1

        # check that it is a palindrome
        while left < right:
            # if not equal then its not
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        
        return True