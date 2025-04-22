class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # left pointer
        l = 0
        # set to check with
        chars = set()
        # max length
        res = 0

        for r in range(len(s)):
            # while the right pointer
            # is in the set
            while s[r] in chars:
                # remove the left
                # until it isnt anymore
                chars.remove(s[l])
                # move the left over after
                # removing it
                l+=1
            # add the right to the chars
            chars.add(s[r])
            # check for a new max length
            res = max(res, r - l + 1)

        return res