class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            # find the middle
            middle = (left+right) // 2

            if nums[middle] == target:
                return middle

            # if the left is less than the middle
            # then we know a series is happening here
            # i.e. in order in that area
            if nums[left] <= nums[middle]:
                # and if the target is greater than the middle
                # or if the target is less than the left
                # then we now it has to be on the right side
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    # else its on the left
                    right = middle - 1
            else:
                # if the target is less than the middle
                # or if target is greater than the right
                # then it will be on the left
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    # else its on the right
                    left = middle + 1
        
        return -1
        