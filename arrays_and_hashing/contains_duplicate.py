
def containsDuplicate(self, nums):
    # set to check dubplicates
    check = set()

    for num in nums:
        # if in the set there is a duplicate
        if num in check:
            return True
        else:
            # if not add it to the set
            check.add(num)
    
    # no duplicates found
    return False