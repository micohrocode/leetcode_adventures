class Solution(object):
    def threeSum(self, nums):
        result = []
        # sort from small to large
        nums.sort()

        for i, val in enumerate(nums):
            # no need to check numbers to the right of 
            # positive numbers as it cant get back to zero
            if val > 0:
                break

            # skip over dubplicates
            if i > 0 and val == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                # check total sum
                total = val + nums[left] + nums[right]

                if total > 0:
                    # if larger than zero move the high side down
                    right -= 1
                elif total < 0:
                    # fi smaller than zero move the low side up
                    left += 1
                else:
                    # else add the result
                    result.append([val,nums[left],nums[right]])
                    # move the pointer to check for more
                    left += 1
                    right -= 1
                    # skip over duplicates
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
            
        return result

        