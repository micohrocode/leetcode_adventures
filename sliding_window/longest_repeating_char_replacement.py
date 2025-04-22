class Solution(object):
    def characterReplacement(self, s, k):
        # keep track of letter counts
        count = {}
        # final max length
        res = 0

        left = 0
        longest = 0

        for right in range(len(s)):
            # add the right to the count
            count[s[right]] = 1 + count.get(s[right],0)

            # max of one character
            longest = max(longest,count[s[right]])

            # check that window is valid
            # and you have enough replacements (k)
            while (right - left + 1) - longest > k:
                count[s[left]] -= 1
                left += 1

            # check for new valid max
            res = max(res, right - left + 1)
        
        return res

        