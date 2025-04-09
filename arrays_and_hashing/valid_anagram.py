def isAnagram(self, s, t):
    # hashmaps to check for letters in each string
    check1 = {}
    check2 = {}

    # if they are different lengths they are not anagrams
    if len(s) != len(t):
        return False

    # add an entry for each letter and keep count
    for i in range(len(s)):
        if s[i] in check1:
            check1[s[i]] += 1
        else:
            check1[s[i]] = 1

        if t[i] in check2:
            check2[t[i]] += 1
        else:
            check2[t[i]] = 1
        
    # check for differences in the letters and counts
    for key in check1.keys():
        if key not in check2.keys():
            return False

        if check1[key] != check2[key]:
            return False
        
    # No differences found
    return True