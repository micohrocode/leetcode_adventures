class Solution(object):
    def findMin(self, nums):
        result = nums[0]
        left = 0
        right = len(nums) - 1

        while left <= right:
            # when the left is less than the right
            # you have found the minimum
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            
            middle = (left + right) // 2
            # check if the middle is the min
            result = min(result, nums[middle])

            if nums[middle] >= nums[left]:
                # the middle is greater than the left
                # so the min is on the right side
                left = middle + 1
            else:
                # the middle is less than the left
                # so the min is on the left side
                right = middle - 1
        
        return result
        