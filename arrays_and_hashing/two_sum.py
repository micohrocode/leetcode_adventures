def twoSum(self, nums, target):
    # hashmap to look for numbers
    check = {}

    for i,v in enumerate(nums):
        # if the number needed is in the hasmap
        # return it
        if target - v in check:
            return [check[target-v],i]
        else:
            # else add the current number to the hashmap
            check[v] = i