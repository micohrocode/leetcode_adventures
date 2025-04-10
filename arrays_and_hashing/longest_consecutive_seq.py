def longestConsecutive(self, nums):
    # remove repeats
    numSet = set(nums)
    longest = 0

    for num in numSet:
        # if its the start of a sequence
        if (num - 1) not in numSet:
            # start its length
            length = 1
            # check for the next number
            while (num + length) in numSet:
                # if there add it to length
                length += 1
            # check for new longest sequence
            longest = max(longest, length)
        
    return longest