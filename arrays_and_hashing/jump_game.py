class Solution(object):
    def canJump(self, nums):
        # goal is first set to the end
        goal = len(nums) - 1

        for i in range(len(nums)-2,-1,-1):
            # if the number plus its index
            # is higher than the goal then it can reach it
            # so the goal is moved to this current index
            # and checked again
            if nums[i] + i >= goal:
                goal = i
        
        # the goal should get down to 0
        # if it can be reached
        return goal == 0