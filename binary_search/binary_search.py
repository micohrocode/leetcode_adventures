class Solution(object):
    def search(self, nums, target):
        # set up left and right at both ends
        left = 0
        right = len(nums) - 1

        while left <= right:
            # get the middle number
            middle = left + ((right-left) // 2)

            # decide which side to go to if not found
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                # number was found, return the index
                return middle
        
        return -1