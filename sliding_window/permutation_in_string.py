class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        # arrays for characters
        s1Count, s2Count = [0]*26, [0]*26
        for i in range(len(s1)):
            # for each character in s1
            # and the same length of s2
            # check for char values
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        # matching values score
        matches = 0
        for i in range(26):
            # count how many match in the first check through
            matches += (1 if s1Count[i] == s2Count[i] else 0)

        l = 0
        # right starts at the first
        # position outside of the 
        # first window length
        for r in range(len(s1), len(s2)):
            if matches == 26:
                # found the permutation
                return True

            # get index for the char (for arrays)
            index = ord(s2[r]) - ord('a')
            # add it to the count
            s2Count[index] += 1

            # check for a match in s1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] + 1 == s2Count[index]:
                # they were equal now they are not
                matches -= 1

            # get index for the char (for arrays)
            index = ord(s2[l]) - ord('a')
            # remove it from the count
            s2Count[index] -= 1

            # check for a match in s1
            if s1Count[index] == s2Count[index]:
                matches += 1
            elif s1Count[index] - 1 == s2Count[index]:
                # they were equal now they are not
                matches -= 1
            
            l += 1

        return matches == 26