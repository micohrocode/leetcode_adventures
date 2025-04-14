class Solution(object):
    def twoSum(self, numbers, target):
        left = 0
        right = len(numbers) - 1

        while left<right:
            # check what you currently are adding
            current = numbers[left] + numbers[right]

            if current > target:
                # if too high go for a lower number
                right -= 1
            elif current < target:
                # if too low go for a higher number
                left += 1
            else:
                return [left+1,right+1]
        
        return []